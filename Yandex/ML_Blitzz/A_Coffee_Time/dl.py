import numpy as np
import lightgbm as lgb
from scipy.special import logsumexp # For numerically stable log(1+exp(x))

# --- Data Loading and Preparation ---

def load_training_data_for_gbt(file_path="restaurants_train.txt"):
    """
    Loads training data from the specified file.
    Each element: {'winner': winner, 'r1': r1, 'd1': d1, 'r2': r2, 'd2': d2, 'id': original_index}
    """
    training_data_list = []
    try:
        with open(file_path, 'r') as f:
            for line_number, line in enumerate(f, 1):
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    try:
                        winner = float(parts[0])
                        r1 = max(0,float(parts[1]))
                        d1 = float(parts[3])
                        r2 = max(0,float(parts[2]))
                        d2 = float(parts[4])
                        # Basic validation
                        if not (0 <= r1 <= 10 and 0 <= r2 <= 10 and \
                                0 <= d1 <= 1 and 0 <= d2 <= 1 and \
                                winner in [0.0, 0.5, 1.0]):
                            # print(f"Warning: Invalid data in train line {line_number}, skipping.")
                            continue
                        training_data_list.append({
                            'winner': winner, 
                            'r1': r1, 'd1': d1, 
                            'r2': r2, 'd2': d2,
                            'id': line_number - 1 # Unique ID for the comparison pair
                        })
                    except ValueError:
                        # print(f"Warning: Value error in train line {line_number}, skipping.")
                        pass 
    except FileNotFoundError:
        print(f"Error: Training file '{file_path}' not found.")
        # In a real scenario, might exit or raise
    return training_data_list

def prepare_data_for_lgbm_ranker(training_data_list):
    """
    Transforms the original training data into a format suitable for LGBMRanker.
    Output:
        X_features (np.array): Feature matrix (rating, distance).
        y_labels (np.array): Relevance labels (e.g., 1 for preferred, 0 for not).
        group_counts (np.array): Number of items in each query/group (always 2 here).
    """
    X_list = []
    y_list = []
    # Each comparison pair is a "query" or "group" for the ranker.
    # All groups will have 2 items (shop1, shop2).
    num_comparisons = len(training_data_list)
    group_counts = np.full(num_comparisons, 2, dtype=int)

    for comp in training_data_list:
        # Features for shop 1 and shop 2
        X_list.append([comp['r1'], comp['d1']]) # Shop 1 features
        X_list.append([comp['r2'], comp['d2']]) # Shop 2 features
        
        winner_label = comp['winner']
        if winner_label == 0.0:  # Shop 1 preferred
            y_list.extend([1, 0]) # Shop 1 is more relevant than Shop 2
        elif winner_label == 1.0:  # Shop 2 preferred
            y_list.extend([0, 1]) # Shop 2 is more relevant than Shop 1
        elif winner_label == 0.5:  # Draw
            y_list.extend([0, 0]) # Both have same (e.g., baseline) relevance.
                                  # This tells the ranker not to try to separate them strongly.
                                  # Alternative: [1,1] - also implies equal relevance.
    
    if not X_list: # Handle empty training data
        return np.array([]), np.array([]), np.array([])

    return np.array(X_list), np.array(y_list), group_counts

# --- GBT Model Training ---

def train_gbt_ranker_model(X_train, y_train, group_train_counts):
    """
    Trains an LGBMRanker model.
    Monotonic constraints: rating (feature 0) increases score, distance (feature 1) decreases score.
    """
    if X_train.shape[0] == 0:
        print("Warning: Empty training data for GBT. Returning None model.")
        return None

    # Hyperparameters need careful tuning based on dataset size and resource limits.
    # These are example values aiming for a relatively small and fast model.
    ranker = lgb.LGBMRanker(
        objective='lambdarank',    # Common pairwise ranking objective
        metric='ndcg',             # Training metric (e.g., ndcg, map). Not the problem's 'm'.
        n_estimators=70,           # Number of trees (keep low for speed/size)
        learning_rate=0.05,        # Learning rate
        num_leaves=15,             # Max leaves (keep low)
        max_depth=4,               # Max depth (keep low)
        min_child_samples=5,       # Min data in a leaf
        subsample=0.8,             # Subsample ratio of the training instance
        colsample_bytree=0.8,      # Subsample ratio of columns when constructing each tree
        # Monotonic constraints: 
        # Feature 0 (rating) should have a positive effect on the score (1).
        # Feature 1 (distance) should have a negative effect on the score (-1).
        monotone_constraints=[1, -1], 
        random_state=42,
        n_jobs=-1 # Use all available cores for training
    )
    
    # print("Training LGBMRanker...")
    ranker.fit(X_train, y_train, group=group_train_counts)
    # print("LGBMRanker training complete.")
    return ranker

# --- 'm' Metric Calculation (using GBT scores) ---

def calculate_m_metric_gbt(original_training_data, gbt_model):
    """
    Calculates the problem-specific 'm' metric using scores from the trained GBT model.
    """
    if gbt_model is None or not original_training_data:
        return float('inf') # Or some other indicator of inability to calculate

    total_loss = 0.0
    num_comparisons = len(original_training_data)

    if num_comparisons == 0:
        return 0.0

    for comp in original_training_data:
        s1_features = np.array([[comp['r1'], comp['d1']]])
        s2_features = np.array([[comp['r2'], comp['d2']]])
        
        # GBT model's predict method outputs raw scores
        s1 = gbt_model.predict(s1_features)[0]
        s2 = gbt_model.predict(s2_features)[0]
        
        winner_label = comp['winner']

        if winner_label == 0.0:  # Shop 1 preferred
            term = s2 - s1
            total_loss += logsumexp([0, term]) 
        elif winner_label == 1.0:  # Shop 2 preferred
            term = s1 - s2
            total_loss += logsumexp([0, term])
        elif winner_label == 0.5:  # Draw
            term1 = s2 - s1
            term2 = s1 - s2
            loss_draw = 0.5 * logsumexp([0, term1]) + 0.5 * logsumexp([0, term2])
            total_loss += loss_draw
            
    return total_loss / num_comparisons

# --- Scoring Test Data ---

def score_test_data_gbt_and_print_results(gbt_model, test_file_path="restaurants.in"):
    """
    Loads test data, scores each coffee shop using the trained GBT model,
    and prints the scores to standard output.
    """
    if gbt_model is None:
        # print("Error: GBT Model is None. Cannot score test data.")
        # Attempt to read N and print default scores if model is missing
        try:
            with open(test_file_path, 'r') as f_test_pre:
                n_str = f_test_pre.readline()
                if n_str:
                    n_items = int(n_str.strip())
                    for _ in range(n_items): print(f"{0.0:.10f}") # Default score
        except: # Fallback if even reading N fails
             pass # Silently fail if cannot determine N
        return

    try:
        with open(test_file_path, 'r') as f:
            try:
                num_shops_str = f.readline()
                if not num_shops_str: # Empty test file
                    # print(f"Warning: Test file '{test_file_path}' is empty or 'N' is missing.")
                    return
                num_shops = int(num_shops_str.strip())
            except ValueError:
                # print(f"Error: Could not parse N from '{test_file_path}'.")
                return # Cannot proceed if N is unknown
                
            for _ in range(num_shops):
                line = f.readline()
                if not line: # Fewer lines than N
                    # print(f"Warning: Test file ended prematurely. Printing default score.")
                    print(f"{0.0:.10f}")
                    continue
                
                parts = line.strip().split('\t') 
                if len(parts) == 2:
                    try:
                        r = float(parts[0])
                        d = float(parts[1])
                        # Basic validation of r,d for sanity, though model should handle values
                        if not (0 <= r <= 10 and 0 <= d <= 1):
                            # print(f"Warning: Out-of-range r/d in test line: {line.strip()}. Scoring as is.")
                            pass
                        
                        shop_features = np.array([[r, d]])
                        shop_score = gbt_model.predict(shop_features)[0]
                        print(f"{shop_score:.10f}") 
                    except ValueError:
                        # print(f"Warning: ValueError parsing r, d in test line: {line.strip()}. Printing default.")
                        print(f"{0.0:.10f}") 
                else:
                    # print(f"Warning: Incorrect format for test line: {line.strip()}. Printing default.")
                    print(f"{0.0:.10f}")
    except FileNotFoundError:
        # print(f"Error: Test file '{test_file_path}' not found.")
        pass # Silently fail if test file is not there, as per some contest systems

# --- Main Execution ---

if __name__ == "__main__":
    training_file_name = "restaurants_train.txt"
    test_input_file_name = "restaurants.in"

    # --- Create dummy files for demonstration (remove for actual submission) ---
    # print("Creating dummy training data...")
    with open(training_file_name, 'w') as f:
        f.write("0.0\t7.5\t0.1\t6.0\t0.2\n")
        f.write("1.0\t5.0\t0.3\t8.0\t0.05\n")
        f.write("0.5\t9.0\t0.15\t9.0\t0.15\n")
        f.write("0.0\t0.0\t0.5\t5.0\t0.6\n") 
        f.write("1.0\t6.0\t0.8\t0.0\t0.1\n") 
        f.write("0.0\t10.0\t0.01\t2.0\t0.9\n")
        f.write("1.0\t2.0\t0.9\t10.0\t0.01\n")
        f.write("0.5\t5.0\t0.5\t5.1\t0.49\n")
        f.write("0.0\t8.0\t0.2\t8.0\t0.3\n") 
        f.write("1.0\t7.0\t0.4\t7.5\t0.4\n")
        # Add more varied data for GBT to learn better
        for i in range(10): # Add more examples
             f.write(f"0.0\t{np.random.uniform(5,10):.1f}\t{np.random.uniform(0,0.3):.2f}\t{np.random.uniform(3,7):.1f}\t{np.random.uniform(0.2,0.5):.2f}\n")
             f.write(f"1.0\t{np.random.uniform(3,7):.1f}\t{np.random.uniform(0.2,0.5):.2f}\t{np.random.uniform(5,10):.1f}\t{np.random.uniform(0,0.3):.2f}\n")
             f.write(f"0.5\t{np.random.uniform(6,8):.1f}\t{np.random.uniform(0.1,0.2):.2f}\t{np.random.uniform(6,8):.1f}\t{np.random.uniform(0.1,0.2):.2f}\n")

    # print("Creating dummy test data...")
    with open(test_input_file_name, 'w') as f:
        f.write("5\n") # Number of test shops
        f.write("7.5\t0.1\n")  # Expected higher score based on first train example
        f.write("6.0\t0.2\n")  # Expected lower score
        f.write("0.0\t0.5\n")  # Shop with missing rating
        f.write("10.0\t0.01\n") # Expected very high score
        f.write("2.0\t0.9\n")   # Expected very low score
    # --- End of dummy file creation ---

    # 1. Load original training data
    original_train_data = load_training_data_for_gbt(training_file_name)

    if not original_train_data:
        # print("No training data loaded. Exiting GBT implementation.")
        # Fallback for scoring: if train fails, GBT model will be None,
        # and score_test_data_gbt_and_print_results handles None model.
        score_test_data_gbt_and_print_results(None, test_input_file_name)

    else:
        # 2. Prepare data for LGBMRanker
        X_train_gbt, y_train_gbt, group_train_gbt = prepare_data_for_lgbm_ranker(original_train_data)

        # 3. Train GBT model
        gbt_model = train_gbt_ranker_model(X_train_gbt, y_train_gbt, group_train_gbt)

        if gbt_model:
            # 4. (Optional) Calculate 'm' on training data using the GBT model
            m_value_gbt = calculate_m_metric_gbt(original_train_data, gbt_model)
            # print(f"\nGBT Model Performance:")
            # print(f"Performance metric 'm' on the training data (using GBT scores): {m_value_gbt:.6f}")
            # Monotonicity is enforced by model constraints. A check could be:
            # test_r_better = 10; test_r_worse = 5; test_d_better = 0.1; test_d_worse=0.5
            # score_good = gbt_model.predict(np.array([[test_r_better, test_d_better]]))[0]
            # score_worse_rating = gbt_model.predict(np.array([[test_r_worse, test_d_better]]))[0]
            # score_worse_dist = gbt_model.predict(np.array([[test_r_better, test_d_worse]]))[0]
            # print(f"Monotonicity check: S(10,0.1)={score_good:.3f}, S(5,0.1)={score_worse_rating:.3f} (should be lower), S(10,0.5)={score_worse_dist:.3f} (should be lower)")
            # assert score_good >= score_worse_rating
            # assert score_good >= score_worse_dist


        # 5. Score test data and print results
        # print("\nScoring test shops with GBT model:")
        score_test_data_gbt_and_print_results(gbt_model, test_input_file_name)