import sys
import numpy as np

def flush_stdout():
    """Helper to ensure we flush after printing predictions."""
    sys.stdout.flush()

def read_floats(n):
    """Reads one line from stdin and parses it into n floats."""
    line = sys.stdin.readline().strip()
    values = list(map(float, line.split()))
    return values

def fit_increment(X, gradient):
    """
    Fits a linear increment model to the provided gradient using least squares.
    For real usage, consider regression trees or other base learners 
    for better performance in gradient boosting.
    """
    grad_target = -gradient  # negative gradient
    XT = X.T
    A = XT @ X
    b = XT @ grad_target
    try:
        w = np.linalg.inv(A) @ b
    except np.linalg.LinAlgError:
        w = np.linalg.pinv(A) @ b
    return w

def adjust_eta(grad, eta, increase_factor=1.05, decrease_factor=0.95, threshold=0.1):
    """
    Adjust the learning rate (eta) based on the gradient magnitude.
    """
    grad_magnitude = np.linalg.norm(grad)
    if grad_magnitude > threshold:
        eta *= increase_factor
    else:
        eta *= decrease_factor
    return eta

def main():
    # -------------------- Step 1: Read input data --------------------
    first_line = sys.stdin.readline().strip()
    N, k, t = map(int, first_line.split())
    
    X_data = []
    for _ in range(N):
        line = sys.stdin.readline().strip()
        feats = list(map(float, line.split()))
        assert len(feats) == k, f"Expected {k} features, got {len(feats)}."
        X_data.append(feats)
    
    X = np.array(X_data)  # shape (N, k)
    
    # -------------------- Step 2: Prepare for iterative boosting --------------------
    increments = []
    eta = 0.1  # Initial learning rate
    
    # -------------------- Step 3: Iterative loop --------------------
    for iteration in range(t):
        # 3a) Compute current predictions
        if iteration == 0:
            preds = np.zeros(N)
        else:
            preds = np.zeros(N)
            for w_k in increments:
                preds += X.dot(w_k)
        
        # 3b) Print predictions for each of the N samples
        print(" ".join(map(str, preds)))
        flush_stdout()
        
        # 3c) If not the last iteration, read derivative/gradient from stdin
        if iteration < t - 1:
            grad = np.array(read_floats(N))
            
            # Adjust the learning rate based on the gradient
            eta = adjust_eta(grad, eta)
            
            # 3d) Fit a linear increment to the negative of this gradient
            w_new = fit_increment(X, grad) * eta
            increments.append(w_new)
        else:
            pass

if __name__ == "__main__":
    main()