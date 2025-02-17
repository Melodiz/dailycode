
import numpy as np
import pandas as pd

class SimpleDecisionStumpRegressor:
    """
    A single-level regression tree (i.e., a stump):
      - Chooses one feature and one threshold that minimize MSE on the *training targets*
        (here, the training targets for the stump are the gradients).
      - Splits data into "left" and "right" leaf nodes.
      - Each leaf has a constant prediction = mean(targets_in_that_leaf).
    """
    def __init__(self):
        self.feature_idx_ = None
        self.threshold_   = None
        self.left_value_  = None
        self.right_value_ = None

    def fit(self, X, y):
        """
        X: DataFrame or 2D NumPy array of shape (n_samples, n_features).
        y: 1D NumPy array of shape (n_samples,). Here y is the gradient (pseudo-residual)
           for this iteration.
        
        Steps:
          1) For each feature, find the best threshold that gives minimal MSE
             on these "targets" (grads).
          2) Store the best feature_idx_ and threshold_.
          3) left_value_  = mean of y where X[:, feature_idx_] <= threshold_
             right_value_ = mean of y otherwise.
        """
        # Convert X to a NumPy array, if it's a Pandas DataFrame
        if isinstance(X, pd.DataFrame):
            X_np = X.values
        else:
            X_np = X
        n_samples, n_features = X_np.shape
        
        best_mse = float("inf")

        for feature_idx in range(n_features):
            x_col = X_np[:, feature_idx]
            unique_vals = np.unique(x_col)
            for val in unique_vals:
                left_mask = (x_col <= val)
                right_mask = ~left_mask

                y_left = y[left_mask]
                y_right = y[right_mask]

                # Compute MSE on each side
                if len(y_left) > 0:
                    mse_left = np.mean((y_left - np.mean(y_left))**2)
                else:
                    mse_left = 0.0
                if len(y_right) > 0:
                    mse_right = np.mean((y_right - np.mean(y_right))**2)
                else:
                    mse_right = 0.0
                
                w_mse = (len(y_left)*mse_left + len(y_right)*mse_right) / n_samples
                
                if w_mse < best_mse:
                    best_mse = w_mse
                    self.feature_idx_ = feature_idx
                    self.threshold_   = val

        # Final left/right means:
        col_final       = X_np[:, self.feature_idx_]
        left_mask_final = (col_final <= self.threshold_)
        right_mask_final = ~left_mask_final
        self.left_value_  = np.mean(y[left_mask_final]) if np.any(left_mask_final) else 0.0
        self.right_value_ = np.mean(y[right_mask_final]) if np.any(right_mask_final) else 0.0

    def predict(self, X):
        """Predict values for each row in X."""
        if isinstance(X, pd.DataFrame):
            X_np = X.values
        else:
            X_np = X
        preds = np.empty(X_np.shape[0])
        col   = X_np[:, self.feature_idx_]
        
        left_mask  = (col <= self.threshold_)
        right_mask = ~left_mask
        
        preds[left_mask]  = self.left_value_
        preds[right_mask] = self.right_value_
        
        return preds


class GradientBoostingRegressorWithCustomGradient:
    """
    Gradient Boosting where, at each iteration, we rely on the user-provided
    get_grad(preds) function to compute the gradient.
    
    Args:
      n_estimators  (int)  : number of boosting iterations (k times).
      learning_rate (float): step size applied to each stump's predictions.

    Workflow at iteration i:
      1) preds_i -> call get_grad(preds_i)               -> grads_i
      2) Fit stump on (X, grads_i). Let's call it stump_i
      3) preds_{i+1} = preds_i + learning_rate * stump_i.predict(X)
    """
    def __init__(self, n_estimators=5, learning_rate=0.1):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.stumps_ = []
        
    def fit(self, X, get_grad):
        """
        X        : DataFrame or 2D NumPy array, shape (n_samples, n_features).
        get_grad : A function that accepts the current predictions (1D array of shape n_samples)
                   and returns the gradient (another 1D array).
                    signature: grads = get_grad(preds)
        
        We do exactly n_estimators calls to get_grad.
        """
        # Initialize predictions to 0 (or you could use the mean of some initial guess)
        if isinstance(X, pd.DataFrame):
            n_samples = X.shape[0]
        else:
            n_samples = X.shape[0]
        self.init_preds_ = np.zeros(n_samples, dtype=float)
        
        current_preds = np.copy(self.init_preds_)
        
        # Clear any previous stumps just in case
        self.stumps_.clear()
        
        for i in range(self.n_estimators):
            # get_grad(...) is provided from outside. We call it on the current predictions.
            grads = get_grad(current_preds)   # shape (n_samples,)

            # Fit a single stump to predict these grads
            stump = SimpleDecisionStumpRegressor()
            stump.fit(X, grads)
            self.stumps_.append(stump)

            # Update current predictions
            update = stump.predict(X)
            current_preds += self.learning_rate * update

    def predict(self, X):
        """
        Combine all stumps' outputs + the initial predictions to get final predictions.
        
        In standard gradient boosting for regression with an MSE-like loss, the sum of
        stump predictions is typically our final F(X).
        
        But note: We do NOT call get_grad here. We only use the learned stumps.
        """
        # Start with init_preds_ = 0 for all samples. 
        # But we don't know how many samples are in X at prediction time, 
        # so we cannot just reuse the same array. We'll do a fresh array of zeros:
        if isinstance(X, pd.DataFrame):
            n_samples = X.shape[0]
        else:
            n_samples = X.shape[0]
        
        preds = np.zeros(n_samples, dtype=float)
        for stump in self.stumps_:
            preds += self.learning_rate * stump.predict(X)
        return preds


# ------------------ Usage Example ------------------

if __name__ == "__main__":
    # Suppose we have a dataset with n=100 samples, m=3 features:
    np.random.seed(42)
    n_samples = 100
    X = np.random.randn(n_samples, 3)
    
    # Let's define some "true" function (unknown to our model) y = 3*x0 - 2*x1 + ...
    # We'll just pick something for demonstration:
    true_y = 3*X[:,0] - 2*X[:,1] + 1.0
    # Add some noise
    y = true_y + np.random.normal(scale=0.5, size=n_samples)
    
    # Convert to a DataFrame if you prefer
    df = pd.DataFrame(X, columns=["feat1","feat2","feat3"])
    df["target"] = y

    # We'll do a train/test split:
    train_df = df.iloc[:80]
    test_df  = df.iloc[80:]
    X_train  = train_df[["feat1","feat2","feat3"]]
    y_train  = train_df["target"].values
    X_test   = test_df[["feat1","feat2","feat3"]]
    y_test   = test_df["target"].values
    
    # Now we define a custom get_grad function.
    # For demonstration, let's just assume we want MSE loss:
    #   MSE loss = 1/2 * (y - preds)^2
    #   derivative w.r.t. preds is (preds - y).
    # So the gradient is
    # (preds - y).
    # But we do NOT do that ourselves; we pretend we only have get_grad. 
    # We'll define get_grad as though we have no direct knowledge of y, 
    # but we do for the example. For a real scenario, you'd encapsulate 
    # whatever logic is needed inside get_grad.
    
    def get_grad_MSE(preds):
        # gradient = (preds - y)
        # we store y_train outside as a closure variable
        return (preds - y_train)
    
    # Create and fit the model
    gbr = GradientBoostingRegressorWithCustomGradient(
        n_estimators=5, 
        learning_rate=0.1
    )
    gbr.fit(X_train, get_grad=get_grad_MSE)
    
    # Predict on test
    y_pred = gbr.predict(X_test)
    
    # Evaluate MSE on test
    mse_test = np.mean((y_pred - y_test)**2)
    print(f"Test MSE = {mse_test:.3f}")