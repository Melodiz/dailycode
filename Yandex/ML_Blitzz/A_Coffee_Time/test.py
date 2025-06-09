import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp # For numerically stable log(1+exp(x))
import math


def load_training_data(file_path="restaurants_train.txt"):
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
                training_data.append({'winner': winner, 'r1': r1, 'd1': d1, 'r2': r2, 'd2': d2})
    return training_data

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

training_data_list = load_training_data()

optimal_wr, optimal_wd, optimal_b = 0.1301726308, 1.5460590234, 0.0000000210
# print current loss
print(f'{loss_function([optimal_wr, optimal_wd, optimal_b], training_data_list) - 0.6575930758932114:.10f}')


def check_stop_condition(training_data_list, params):
    for comp in training_data_list:
        if comp['r1'] > 0 and comp['r2'] > 0:
            winner = comp['r1'] > comp['r2'] and comp['d1'] < comp['d2']
            score1 = score_function(params, comp['r1'], comp['d1'])
            score2 = score_function(params, comp['r2'], comp['d2'])
            if winner and score1 < score2:
                print(comp, score1, score2)

def compute_m(training_data_list, params):
    results = []
    for comp in training_data_list:
        if comp['winner'] != 0.5:
            s1 = score_function(params, comp['r1'], comp['d1'])
            s2 = score_function(params, comp['r2'], comp['d2'])
            scrore_loser = min(s1, s2)
            score_winner = max(s1, s2)
            results.append((scrore_loser, score_winner))
    m = 0 
    for s_loser, s_winner in results:
        m += math.log(1 + math.exp(s_loser - s_winner))
    return m/len(results)

print(compute_m(training_data_list, [0.1301726308, 1.5460590234, 0.0000000210]))
