import pandas as pd
import numpy as np
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import VotingClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform, randint
import warnings
warnings.filterwarnings('ignore')

# Load data
print("Loading data...")
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# Separate features and target
X = train_df.drop('target', axis=1, errors='ignore')
y = train_df['target'] if 'target' in train_df.columns else None

# Check for class imbalance
print(f"Class distribution: {pd.Series(y).value_counts()}")
print(f"Total features: {X.shape[1]}")

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training set shape: {X_train.shape}")
print(f"Validation set shape: {X_val.shape}")

# Feature Engineering
print("\n--- Feature Engineering ---")
# Create polynomial features for interactions
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_val_poly = poly.transform(X_val)
poly_feature_names = poly.get_feature_names_out(X.columns)
print(f"Polynomial features shape: {X_train_poly.shape}")

# Feature selection to avoid curse of dimensionality
k_best = min(100, X_train_poly.shape[1])  # Select top features
selector = SelectKBest(mutual_info_classif, k=k_best)
X_train_selected = selector.fit_transform(X_train_poly, y_train)
X_val_selected = selector.transform(X_val_poly)
selected_indices = selector.get_support(indices=True)
selected_feature_names = poly_feature_names[selected_indices]
print(f"Selected {len(selected_feature_names)} features")

# Handle class imbalance if needed
class_counts = pd.Series(y_train).value_counts()
if class_counts.min() / class_counts.max() < 0.75:  # If imbalanced
    print("Applying SMOTE for class balance...")
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train_selected, y_train)
    print(f"After SMOTE: {pd.Series(y_train_balanced).value_counts()}")
else:
    X_train_balanced = X_train_selected
    y_train_balanced = y_train

# Advanced Hyperparameter Tuning
print("\n--- Advanced Hyperparameter Tuning ---")
param_distributions = {
    'learning_rate': uniform(0.01, 0.1),
    'depth': randint(4, 10),
    'l2_leaf_reg': uniform(1, 10),
    'random_strength': uniform(0.1, 1.0),
    'bagging_temperature': uniform(0, 1),
    'scale_pos_weight': uniform(0.8, 1.2),
    'iterations': [2000]  # Fixed for faster search
}

# Use stratified k-fold for more reliable CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Randomized search with cross-validation
print("Starting hyperparameter search (this may take some time)...")
random_search = RandomizedSearchCV(
    CatBoostClassifier(verbose=0, eval_metric='AUC', random_seed=42),
    param_distributions=param_distributions,
    n_iter=20,  # Number of parameter settings sampled
    cv=cv,
    scoring='roc_auc',  # AUC is more robust than accuracy
    random_state=42,
    n_jobs=-1,
    verbose=1
)

random_search.fit(X_train_balanced, y_train_balanced)
print(f"\nBest parameters: {random_search.best_params_}")
print(f"Best cross-validation score: {random_search.best_score_:.4f}")

# Train CatBoost with best parameters
print("\n--- Training Final CatBoost Model ---")
catboost_model = CatBoostClassifier(
    iterations=5000,
    learning_rate=random_search.best_params_['learning_rate'],
    depth=random_search.best_params_['depth'],
    l2_leaf_reg=random_search.best_params_['l2_leaf_reg'],
    random_strength=random_search.best_params_['random_strength'],
    bagging_temperature=random_search.best_params_['bagging_temperature'],
    scale_pos_weight=random_search.best_params_['scale_pos_weight'],
    loss_function='Logloss',
    eval_metric='AUC',
    random_seed=42,
    early_stopping_rounds=300,
    verbose=100
)

# Create CatBoost Pool for better performance
train_pool = Pool(X_train_balanced, y_train_balanced)
val_pool = Pool(X_val_selected, y_val)

# Train with early stopping
catboost_model.fit(train_pool, eval_set=val_pool, use_best_model=True, plot=True)

# Train additional models for ensemble
print("\n--- Training Additional Models for Ensemble ---")
lgbm_model = LGBMClassifier(
    n_estimators=2000,
    learning_rate=random_search.best_params_['learning_rate'],
    num_leaves=2**random_search.best_params_['depth'],
    max_depth=random_search.best_params_['depth'],
    reg_lambda=random_search.best_params_['l2_leaf_reg'],
    random_state=42,
    verbose=-1
)

xgb_model = XGBClassifier(
    n_estimators=2000,
    learning_rate=random_search.best_params_['learning_rate'],
    max_depth=random_search.best_params_['depth'],
    reg_lambda=random_search.best_params_['l2_leaf_reg'],
    random_state=42,
    verbosity=0
)

# Train models
print("Training LightGBM...")
lgbm_model.fit(
    X_train_balanced, y_train_balanced,
    eval_set=[(X_val_selected, y_val)],
    early_stopping_rounds=100,
    verbose=False
)

print("Training XGBoost...")
xgb_model.fit(
    X_train_balanced, y_train_balanced,
    eval_set=[(X_val_selected, y_val)],
    early_stopping_rounds=100,
    verbose=False
)

# Create voting ensemble
print("\n--- Creating Ensemble ---")
ensemble = VotingClassifier(
    estimators=[
        ('catboost', catboost_model),
        ('lgbm', lgbm_model),
        ('xgb', xgb_model)
    ],
    voting='soft'  # Use probability predictions
)

# Train ensemble
ensemble.fit(X_train_balanced, y_train_balanced)

# Evaluate individual models
print("\n--- Model Evaluation ---")
models = {
    'CatBoost': catboost_model,
    'LightGBM': lgbm_model,
    'XGBoost': xgb_model,
    'Ensemble': ensemble
}

results = {}
for name, model in models.items():
    # Get predictions
    val_preds_proba = model.predict_proba(X_val_selected)[:, 1]
    val_preds = (val_preds_proba > 0.5).astype(int)
    
    # Calculate metrics
    accuracy = accuracy_score(y_val, val_preds)
    auc = roc_auc_score(y_val, val_preds_proba)
    
    print(f"\n{name} Metrics:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC AUC: {auc:.4f}")
    
    results[name] = {
        'accuracy': accuracy,
        'auc': auc,
        'model': model
    }

# Find best model based on AUC
best_model_name = max(results, key=lambda x: results[x]['auc'])
best_model = results[best_model_name]['model']
print(f"\nBest model: {best_model_name} with AUC: {results[best_model_name]['auc']:.4f}")

# Feature importance for CatBoost
if 'CatBoost' in models:
    feature_importance = catboost_model.get_feature_importance()
    importance_df = pd.DataFrame({
        'Feature': selected_feature_names,
        'Importance': feature_importance
    })
    importance_df = importance_df.sort_values('Importance', ascending=False)
    
    print("\nTop 10 Important Features:")
    print(importance_df.head(10))
    
    # Plot feature importance
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Importance', y='Feature', data=importance_df.head(20))
    plt.title('Top 20 Feature Importance')
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    print("Feature importance plot saved to 'feature_importance.png'")

# Process test data
print("\n--- Making Test Predictions ---")
X_test_poly = poly.transform(test_df)
X_test_selected = selector.transform(X_test_poly)

# Make predictions with best model
test_preds_proba = best_model.predict_proba(X_test_selected)[:, 1]
test_preds = (test_preds_proba > 0.5).astype(int)

# Create submission dataframe with integer predictions
submission = pd.DataFrame({
    'id': test_df.index,
    'prediction': test_preds
})

# Save predictions to file
submission.to_csv('catboost_submission.csv', index=False)
print("\nPredictions saved to 'catboost_submission.csv' with integer predictions (0 or 1)")

# If you need to save the probabilities as well for reference
proba_submission = pd.DataFrame({
    'id': test_df.index,
    'prediction_probability': test_preds_proba
})
proba_submission.to_csv('catboost_proba_submission.csv', index=False)
print("Probability predictions saved to 'catboost_proba_submission.csv'")

# Try different thresholds to optimize accuracy
print("\n--- Threshold Optimization ---")
thresholds = np.arange(0.3, 0.7, 0.05)
threshold_results = []

for threshold in thresholds:
    val_preds_threshold = (results[best_model_name]['model'].predict_proba(X_val_selected)[:, 1] > threshold).astype(int)
    accuracy = accuracy_score(y_val, val_preds_threshold)
    threshold_results.append((threshold, accuracy))

best_threshold = max(threshold_results, key=lambda x: x[1])
print(f"Best threshold: {best_threshold[0]:.2f} with accuracy: {best_threshold[1]:.4f}")

# Apply best threshold to test predictions
optimized_test_preds = (test_preds_proba > best_threshold[0]).astype(int)

# Create optimized submission
optimized_submission = pd.DataFrame({
    'id': test_df.index,
    'prediction': optimized_test_preds
})

# Save optimized predictions
optimized_submission.to_csv('optimized_submission.csv', index=False)
print("Optimized predictions saved to 'optimized_submission.csv'")

# Save predictions in the required format (only binary predictions without headers and id column)
np.savetxt('binary_predictions.txt', optimized_test_preds, fmt='%d')
print("Binary predictions saved to 'binary_predictions.txt' (no headers, no id column)")

print("\n--- Process Complete ---")