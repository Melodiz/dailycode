import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ------------------ 1) Synthesize data  ------------------
np.random.seed(42)
n_samples = 750
n_features = 20

X = np.random.randn(n_samples, n_features)
# Suppose the true function is a linear combination of the first 5 features plus some noise
true_y = 3*X[:,0] - 2*X[:,1] + X[:,2] - 1.5*X[:,3] + 0.5*X[:,4] + 1.0
y = true_y + np.random.normal(scale=0.5, size=n_samples)

# Use a Pandas DataFrame for convenience
feature_names = [f"feat{i+1}" for i in range(n_features)]
df = pd.DataFrame(X, columns=feature_names)
df["target"] = y

# Train/test split
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
X_train = train_df[feature_names]
y_train = train_df["target"].values
X_test  = test_df[feature_names]
y_test  = test_df["target"].values

# ------------------ 2) Create DMatrix for XGBoost  ------------------
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest  = xgb.DMatrix(X_test,  label=y_test)

# ------------------ 3) Define a custom objective function  ------------------
# We'll mimic MAE. 
# For MAE, the loss is |pred - label|
#   => grad = sign(pred - label)
#   => hess = 0 (not defined at pred = label, so we use a small constant)

def custom_obj(preds, dtrain):
    labels = dtrain.get_label()
    diff = preds - labels
    grad = np.sign(diff)
    hess = np.ones_like(grad) * 0.001  # small constant for numerical stability
    return grad, hess

# ------------------ 4) Train the model using XGBoost  ------------------
params = {
    "max_depth": 5,          # increased depth due to more features
    "eta": 0.1,              # learning rate
    "verbosity": 1,          # silent
    "objective": "reg:squarederror",  
    "subsample": 0.8,        # added subsampling for better generalization
    "colsample_bytree": 0.8  # added column sampling for better generalization
}

num_boost_round = 30  # increased number of rounds due to more complex data

bst = xgb.train(
    params=params,
    dtrain=dtrain,
    num_boost_round=num_boost_round,
    obj=custom_obj,           # Our custom gradient & hessian
    evals=[(dtrain, "train"), (dtest, "test")],
    early_stopping_rounds=10      # optional early stopping
)

# ------------------ 5) Predict & evaluate  ------------------
y_pred = bst.predict(dtest)
mse = mean_squared_error(y_test, y_pred)
print(f"Test MSE = {mse:.4f}")

# ------------------ 6) Feature Importance  ------------------
importance = bst.get_score(importance_type='gain')
importance = sorted(importance.items(), key=lambda x: x[1], reverse=True)
print("\nTop 5 important features:")
for feat, score in importance[:5]:
    print(f"{feat}: {score}")