import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp # For numerically stable log(1+exp(x))

# Global optimal parameters to be set after training
# These will store the learned weights and bias
optimal_wr = 0.0
optimal_wd = 0.0
optimal_b = 0.0

# 1. Score Function Definition
def score_function(params, r, d):
    """
    Calculates the goodness score for a coffee shop.
    S(r,d) = wr * r - wd * d + b
    """
    wr, wd, b = params
    return wr * r - wd * d + b

# 2. Loss Function for Training
def loss_function(params, training_data_list):
    """
    Calculates the average logistic loss over the training dataset.
    This is the performance metric 'm' to be minimized.
    """
    total_loss = 0.0
    num_comparisons = len(training_data_list)

    if num_comparisons == 0:
        return 0.0

    # wr, wd, b = params # Parameters are directly passed
    # Monotonicity constraints (wr >= 0, wd >= 0) are handled by the optimizer's bounds.

    for comp in training_data_list:
        s1 = score_function(params, comp['r1'], comp['d1'])
        s2 = score_function(params, comp['r2'], comp['d2'])
        winner_label = comp['winner']

        if winner_label == 0.0:  # Shop 1 preferred
            # Loss term: log(1 + exp(s2 - s1))
            term = s2 - s1
            total_loss += logsumexp([0, term]) # Numerically stable version
        elif winner_label == 1.0:  # Shop 2 preferred
            # Loss term: log(1 + exp(s1 - s2))
            term = s1 - s2
            total_loss += logsumexp([0, term]) # Numerically stable version
        elif winner_label == 0.5:  # Draw
            # Loss term: 0.5 * log(1 + exp(s2 - s1)) + 0.5 * log(1 + exp(s1 - s2))
            term1 = s2 - s1
            term2 = s1 - s2
            loss_draw = 0.5 * logsumexp([0, term1]) + 0.5 * logsumexp([0, term2])
            total_loss += loss_draw
        # else: Malformed winner label, skip or error. Assuming valid input.
            
    return total_loss / num_comparisons

# 3. Data Preprocessing (Training Data)
def load_training_data(file_path="restaurants_train.txt"):
    """
    Loads training data from the specified file.
    Each line: winner r1 d1 r2 d2 (tab-separated)
    """
    training_data = []
    with open(file_path, 'r') as f:
        for line_number, line in enumerate(f, 1):
            parts = line.strip().split('\t')
            if len(parts) == 5:
                winner = float(parts[0])
                r1 = max(float(parts[1]), 0)
                r2 = max(float(parts[2]), 0)
                d1 = max(float(parts[3]), 0)
                d2 = max(float(parts[4]), 0)
                
                # Ratings r1, r2: 0-10. Distances d1, d2: 0-1. Winner: 0.0, 0.5, 1.0.
                if not (0 <= r1 <= 10 and 0 <= r2 <= 10 and \
                        0 <= d1 <= 1 and 0 <= d2 <= 1 and \
                        winner in [0.0, 0.5, 1.0]):
                    print(f"Warning: Invalid data values in line {line_number}: {line.strip()}")
                    exit(1)

                training_data.append({'winner': winner, 'r1': r1, 'd1': d1, 'r2': r2, 'd2': d2})
    return training_data

# 4. Model Training
def train_model(training_data_list):
    """
    Trains the linear model by minimizing the loss function.
    Sets the global optimal_wr, optimal_wd, optimal_b.
    """
    global optimal_wr, optimal_wd, optimal_b
    
    if not training_data_list:
        print("Error: No training data provided to train_model.")
        # Set default parameters or handle as failure
        optimal_wr, optimal_wd, optimal_b = 1.0, 1.0, 0.0 # Default/fallback parameters
        print("Warning: Using default parameters as training data is empty.")
        return

    # Initial guesses for wr, wd, b
    initial_params = np.array([1.0, 1.0, 0.0])  
    
    # Bounds for parameters: wr >= 0, wd >= 0, b is unbounded
    bounds = [(0, None), (0, None), (None, None)] 

    # Minimize the loss function using L-BFGS-B
    result = minimize(loss_function, 
                      initial_params, 
                      args=(training_data_list,), 
                      method='L-BFGS-B', 
                      bounds=bounds,
                      options={'maxiter': 1000, 'disp': False, 'ftol': 1e-9, 'gtol': 1e-7}) # Standard options

    if result.success:
        optimal_params = result.x
        optimal_wr, optimal_wd, optimal_b = optimal_params[0], optimal_params[1], optimal_params[2]
        
        # Monotonicity check (L-BFGS-B with bounds should ensure this)
        # Allowing for very small negative values due to numerical precision.
        if optimal_wr < -1e-6 or optimal_wd < -1e-6:
             # This is critical as non-monotonic solutions get 0 points.
             print(f"CRITICAL ERROR: Monotonicity violated by learned weights: wr={optimal_wr:.4f}, wd={optimal_wd:.4f}.")
             print("This solution would receive 0 points. Aborting.")
             exit(1) # Abort if monotonicity is violated
        
        # print(f"Training successful. Optimal parameters: wr={optimal_wr:.4f}, wd={optimal_wd:.4f}, b={optimal_b:.4f}")
        # print(f"Minimized loss (m): {result.fun:.6f}")
    else:
        print(f"Error: Optimization failed to converge. Message: {result.message}")
        # Fallback to initial or default parameters if optimization fails.
        # For this problem, successful optimization is crucial.
        optimal_wr, optimal_wd, optimal_b = initial_params[0], initial_params[1], initial_params[2]
        print(f"Warning: Using initial parameters due to optimization failure: wr={optimal_wr}, wd={optimal_wd}, b={optimal_b}")
        # Depending on requirements, might need to exit(1) here too.
        # For now, allow scoring with initial params but flag it.

# 5. Scoring Test Instances
def score_test_data_and_print_results(test_file_path="restaurants.in"):
    """
    Loads test data, scores each coffee shop using the trained model,
    and prints the scores.
    """
    # Ensure model has been "trained" (parameters are set)
    current_params = (optimal_wr, optimal_wd, optimal_b)
    # print(f"Using parameters for scoring: wr={optimal_wr:.4f}, wd={optimal_wd:.4f}, b={optimal_b:.4f}")


    try:
        with open(test_file_path, 'r') as f:
            try:
                # First line is the number of coffee shops
                num_shops_str = f.readline()
                if not num_shops_str: # Empty file or first line missing
                    print(f"Error: Test file '{test_file_path}' is empty or 'N' is missing.")
                    return
                num_shops = int(num_shops_str.strip())
            except ValueError:
                print(f"Error: Could not parse the number of test instances from '{test_file_path}'.")
                return
                
            for line_number, line in enumerate(f, 1):
                parts = line.strip().split('\t') # Assuming tab-separated for consistency
                if len(parts) == 2:
                    try:
                        r = float(parts[0])
                        d = float(parts[1])

                        # Validate r and d ranges if necessary (0-10 for r, 0-1 for d)
                        if not (0 <= r <= 10 and 0 <= d <= 1):
                            # print(f"Warning: Invalid r/d values in test line {line_number}: {line.strip()}. Scoring with values as is.")
                            pass # Or assign a default score / error

                        shop_score = score_function(current_params, r, d)
                        print(f"{shop_score:.10f}") # Output score with specified precision
                    except ValueError:
                        # print(f"Warning: Could not parse r, d in test line {line_number}: {line.strip()}. Skipping.")
                        # Outputting a default score or error marker might be required by problem spec
                        print(f"{0.0:.10f}") # Or handle error appropriately
                else:
                    # print(f"Warning: Incorrect format for test line {line_number}: {line.strip()}. Skipping.")
                    print(f"{0.0:.10f}") # Or handle error appropriately
    except FileNotFoundError:
        print(f"Error: Test file '{test_file_path}' not found.")

# Main execution block
if __name__ == "__main__":
    # Define standard file names as per the problem description
    training_file_name = "restaurants_train.txt"
    # test_input_file_name = "restaurants.in"

    # Step 1: Load training data
    training_data_list = load_training_data(training_file_name)
    print(len(training_data_list))
    print(training_data_list[0])
    
    # Step 2: Train the model
    # The train_model function will set global optimal_wr, optimal_wd, optimal_b
    # if training_data_list: # Only train if there's data
    #     train_model(training_data_list)
    # else:
    #     # If no training data, use default parameters (or handle error)
    #     print("Warning: No training data loaded. Using default parameters for scoring (wr=1, wd=1, b=0).")
    #     optimal_wr, optimal_wd, optimal_b = 1.0, 1.0, 0.0 # Fallback

    # Step 3: Score test data and print results
    # score_test_data_and_print_results(test_input_file_name)