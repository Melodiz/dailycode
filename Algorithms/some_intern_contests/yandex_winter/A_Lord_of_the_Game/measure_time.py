import time
import random
from solution import solve
from tqdm import tqdm

def generate_max_input():
    n = 10**5 - 1  # Maximum n is just under 10^5
    values = [random.randint(1, 10**9) for _ in range(n)]  # Assuming max value of 10^9
    return n, values

def brute_force_max_score(piles):
    n = len(piles)
    min_val, max_val = min(piles), max(piles)
    max_score = 0
    for emci in tqdm(range(n), desc="Brute-force solution"):
        for raid in range(n):
            if piles[emci] == min_val and piles[raid] == max_val:
                score = sum(piles[min(emci, raid):max(emci, raid)+1])
                max_score = max(max_score, score)
    return max_score

def check_extreme_input():
    print("Generating extreme input...")
    n, values = generate_max_input()
    print(f"Input size: {n}")

    print("\nRunning optimized solution...")
    start_time = time.time()
    optimized_result = solve(values, n)
    optimized_time = time.time() - start_time
    print(f"Optimized solution time: {optimized_time:.6f} seconds")
    print(f"Optimized result: {optimized_result}")

    print("\nRunning brute-force solution (this may take a very long time)...")
    start_time = time.time()
    brute_force_result = brute_force_max_score(values)
    brute_force_time = time.time() - start_time
    print(f"Brute-force solution time: {brute_force_time:.6f} seconds")
    print(f"Brute-force result: {brute_force_result}")

    if optimized_result == brute_force_result:
        print("\nExtreme input check: PASSED")
    else:
        print("\nExtreme input check: FAILED")

if __name__ == "__main__":
    print("Warning: This test will run on the largest possible input.")
    print("The brute-force solution may take an extremely long time to complete.")
    input("Press Enter to continue or Ctrl+C to abort...")
    
    check_extreme_input()