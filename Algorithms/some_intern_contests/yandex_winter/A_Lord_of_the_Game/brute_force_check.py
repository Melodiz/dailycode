import random
from tqdm import tqdm

# Brute force solution
def calculate_score(piles, emci, raid):
    start = min(emci, raid)
    end = max(emci, raid)
    return sum(piles[start:end+1])

def brute_force_max_score(piles):
    n = len(piles)
    max_score = 0

    for emci in range(n):
        for raid in range(n):
            if piles[emci] == min(piles) and piles[raid] == max(piles):
                score = calculate_score(piles, emci, raid)
                max_score = max(max_score, score)

    return max_score

# Optimized solution
def find_min_max(values):
    min_val, max_val = float('inf'), float('-inf')
    for i in range(len(values)):
        if values[i] < min_val:
            min_val = values[i]
        if values[i] > max_val:
            max_val = values[i]
    return min_val, max_val

def solve(values, n):
    min_val, max_val = find_min_max(values)
    # first variant : left_index < right_index
    left_index, right_index = -1, -1
    result = 0
    for i in range(n):
        if values[i] == min_val:
            left_index = i
            break
    for i in range(n - 1, -1, -1):
        if values[i] == max_val:
            right_index = i
            break
    result = sum(values[min(left_index, right_index):max(right_index, left_index) + 1])
    # second variant : left_index > right_index
    left_index, right_index = -1, -1
    for i in range(n-1, -1, -1):
        if values[i] == min_val:
            left_index = i
            break
    for i in range(n):
        if values[i] == max_val:
            right_index = i
            break
    result = max(sum(values[min(left_index, right_index):max(right_index, left_index) + 1]), result)
    return result 

# Test function
def run_tests(num_tests):
    for test in tqdm(range(1, num_tests + 1)):
        # Generate random test case
        n = random.randint(2, 100)  # Adjust the upper bound as needed
        piles = [random.randint(1, 10) for _ in range(n)]  # Adjust the range as needed

        # Run both solutions
        brute_force_result = brute_force_max_score(piles)
        optimized_result = solve(piles, n)

        # Compare results
        if brute_force_result == optimized_result:
            pass
        else:
            print(f"Test {test}: FAILED")
            print(f"Input: {piles}")
            print(f"Brute Force: {brute_force_result}")
            print(f"Optimized: {optimized_result}")
            return False

    print("All tests passed!")
    return True

if __name__ == "__main__":
    run_tests(10000)