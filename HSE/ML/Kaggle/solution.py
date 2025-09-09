#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder, PolynomialFeatures
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.model_selection import KFold, cross_val_score, GridSearchCV

DATA_PATH = "/Users/ianovosad/code/HSE/ML/Kaggle/XY_diamonds.csv"
SUBMISSION_PATH = "/Users/ianovosad/code/HSE/ML/Kaggle/baseline.csv"


class FeatureBuilder(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        Xc = X.copy()
        # Numeric coercion for safety
        for col in ["carat", "depth", "table", "x", "y", "z"]:
            if col in Xc.columns:
                Xc[col] = pd.to_numeric(Xc[col], errors="coerce")
        # Engineered features
        Xc["volume"] = (Xc[["x", "y", "z"]].product(axis=1)
                         if all(c in Xc.columns for c in ["x", "y", "z"]) else np.nan)
        Xc["carat_sq"] = Xc["carat"] ** 2 if "carat" in Xc.columns else np.nan
        Xc["log_carat"] = np.log1p(Xc["carat"]) if "carat" in Xc.columns else np.nan
        Xc["depth_to_table"] = (
            Xc["depth"] / Xc["table"] if all(c in Xc.columns for c in ["depth", "table"]) else np.nan
        )
        return Xc


def build_submission_from_preds(preds: np.ndarray, n_rows: int) -> pd.DataFrame:
    sub = pd.DataFrame({
        "id": np.arange(1, n_rows + 1, dtype=int),
        "price": preds,
    })
    sub["price"] = sub["price"].clip(lower=10).round(2)
    return sub


def main() -> None:
    raw = pd.read_csv(DATA_PATH)
    print("Loaded:", raw.shape, list(raw.columns))

    has_price = raw["price"].notna()
    print("Labeled rows:", has_price.sum(), "/", len(raw))

    train_df = raw.loc[has_price].copy()
    test_df = raw.loc[~has_price].copy()

    all_features = [c for c in raw.columns if c != "price"]

    # Define ordinals consistent with domain knowledge
    cut_order = ["F", "G", "V", "P", "I"]  # Fair < Good < VeryGood < Premium < Ideal
    color_order = ["J", "I", "H", "G", "F", "E", "D"]  # worse -> best
    clarity_order = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]  # worse -> best

    num_base = [c for c in all_features if c in ["carat", "depth", "table", "x", "y", "z", "volume", "carat_sq", "log_carat", "depth_to_table"]]
    # After FeatureBuilder runs, engineered columns appear; ColumnTransformer selects by name that will exist.

    ordinal_features = [c for c in all_features if c in ["cut", "color", "clarity"]]
    other_cats = [c for c in all_features if c not in num_base + ordinal_features]

    print("Base numeric + engineered (will exist post-transform):", num_base)
    print("Ordinal cats:", ordinal_features)
    print("Other cats (one-hot):", other_cats)

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("poly", PolynomialFeatures(degree=1, include_bias=False)),  # tuned to 1 or 2
            ("scaler", StandardScaler(with_mean=True, with_std=True)),
        ]
    )

    ordinal_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            (
                "encoder",
                OrdinalEncoder(
                    categories=[
                        cut_order if "cut" in ordinal_features else None,
                        color_order if "color" in ordinal_features else None,
                        clarity_order if "clarity" in ordinal_features else None,
                    ][: len(ordinal_features)],
                    handle_unknown="use_encoded_value",
                    unknown_value=-1,
                ),
            ),
            ("scaler", StandardScaler(with_mean=True, with_std=True)),
        ]
    )

    onehot_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, num_base),
            ("ord", ordinal_pipeline, ordinal_features),
            ("cat", onehot_pipeline, other_cats),
        ],
        remainder="drop",
    )

    # Model candidates (linear family only per rules)
    model = Ridge(random_state=42)

    pipe = Pipeline(
        steps=[
            ("features", FeatureBuilder()),
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )

    if len(train_df) > 0:
        X_train = train_df[all_features]
        y_train = train_df["price"].astype(float)

        # Hyperparameter and variant tuning, optimized by MAE
        param_grid = {
            "preprocess__num__poly__degree": [1, 2],
            "model__alpha": [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0],
        }
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        grid = GridSearchCV(
            pipe,
            param_grid=param_grid,
            scoring="neg_mean_absolute_error",
            cv=kf,
            n_jobs=-1,
            verbose=0,
        )
        grid.fit(X_train, y_train)
        best_pipe = grid.best_estimator_
        print("Best params:", grid.best_params_)
        print(f"Best CV MAE: {-grid.best_score_:.2f}")

        # Report RMSE and MAE for the best pipeline
        mse_scores = cross_val_score(best_pipe, X_train, y_train, cv=kf, scoring="neg_mean_squared_error", n_jobs=-1)
        rmse_scores = np.sqrt(-mse_scores)
        mae_scores = -cross_val_score(best_pipe, X_train, y_train, cv=kf, scoring="neg_mean_absolute_error", n_jobs=-1)
        print(f"CV RMSE (best): mean={rmse_scores.mean():.2f}, std={rmse_scores.std():.2f}")
        print(f"CV MAE  (best): mean={mae_scores.mean():.2f}, std={mae_scores.std():.2f}")

        # Fit on all labeled data
        best_pipe.fit(X_train, y_train)

        if len(test_df) > 0:
            preds = best_pipe.predict(test_df[all_features])
            submission = build_submission_from_preds(preds, len(test_df))
            submission.to_csv(SUBMISSION_PATH, index=False)
            print("Saved improved submission to:", SUBMISSION_PATH, submission.shape)
        else:
            print("No unlabeled rows to predict.")
    else:
        # No labels -> heuristic baseline
        df = raw.copy()
        for col in ["carat", "depth", "table", "x", "y", "z"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        volume = df[["x", "y", "z"]].product(axis=1)
        price_est = 4000 * df["carat"].fillna(df["carat"].median()) + 0.1 * volume.fillna(
            volume.median()
        )
        price_est = price_est.clip(lower=100, upper=50000)

        submission = build_submission_from_preds(price_est.values, len(df))
        submission.to_csv(SUBMISSION_PATH, index=False)
        print("No labels found. Wrote baseline-style submission:", SUBMISSION_PATH, submission.shape)


if __name__ == "__main__":
    main()
