import time
import random

def precompute_three_bit_numbers(limit=10**18):
    candidates = []
    # We'll consider bit positions from 0 to 59
    for i in range(60):
        for j in range(i+1, 60):
            for k in range(j+1, 60):
                # Construct the number with bits i, j, k set
                val = (1 << i) + (1 << j) + (1 << k)
                if val <= limit:
                    candidates.append(val)
    candidates.sort()
    return candidates

def solve_query(x, candidates):
    # Standard binary search for the largest value <= x
    # (Python’s bisect or “lower_bound - 1” approach)
    import bisect
    idx = bisect.bisect_right(candidates, x) - 1
    return candidates[idx] if idx >= 0 else 0  # If no candidate is <= x, return 0 or handle appropriately.


# Usage example:
candidates = precompute_three_bit_numbers()
# Then for each query x:
answer = solve_query(x, candidates)
print(answer)

def brute(x):
    current = x
    
    while current >= 0:
        binary = bin(current)[2:] # remove prefix '0b'
        if binary.count('1') == 3:
            return current
        current -= 1
    
    return -1

def generate_test_cases(num_cases, max_budget):
    return [random.randint(1, max_budget) for _ in range(num_cases)]

def test_solutions(num_cases=10**3, max_budget=10**18):
    budgets = generate_test_cases(num_cases, max_budget)
    start_time = time.time()
    for budget in budgets:
        # start_time = time.time()
        result_optimized = find_closest_binary(budget)
        # optimized_time = time.time() - start_time

        # start_time = time.time()
        result_brute_force = brute(budget)
        # brute_force_time = time.time() - start_time

        # assert result_optimized == result_brute_force, f"Mismatch for budget {budget}: Optimized={result_optimized}, Brute Force={result_brute_force}"
    optimized_time = time.time() - start_time
    print(f'Optimized Time: {optimized_time:.6f}')

if __name__ == "__main__":
    test_solutions()