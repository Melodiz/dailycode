import random
from collections import Counter
import time

# Optimal solution from solution.py
def optimal_solution(arr, n):
    arr_copy = arr.copy()
    arr_copy.sort(reverse=True)
    unique = set(arr_copy)
    cnt = Counter(arr_copy)
    for i in range(n):
        if cnt[arr_copy[i]] == 1:
            continue
        cnt[arr_copy[i]] -= 1
        while arr_copy[i] in unique and arr_copy[i] > 0:
            arr_copy[i] //= 2
        unique.add(arr_copy[i])
    return len(set(arr_copy))

# Brute force solution from brute_force.py
def brute_force_solution(arr, n):
    arr_copy = arr.copy()
    cnt = Counter(arr_copy)
    while max(cnt.values()) > 1:
        max_val, max_index = -1, -1
        for i in range(len(arr_copy)):
            if cnt[arr_copy[i]] > 1 and arr_copy[i] > max_val:
                max_val, max_index = arr_copy[i], i
        if max_val < 1: return(len(cnt.keys()))
        tmp = arr_copy[max_index] // 2
        cnt[arr_copy[max_index]] -= 1
        arr_copy[max_index] = tmp
        cnt[tmp] = cnt.get(tmp, 0) + 1
    return len(cnt.keys())

def generate_test_case(n, max_val=10**9):
    """Generate a random test case with n elements"""
    return [random.randint(1, max_val) for _ in range(n)]

def run_tests(num_tests=100, max_n=100, max_val=10**6):
    """Run multiple tests and compare solutions"""
    for test_num in range(1, num_tests + 1):
        # Generate random test case
        n = random.randint(1, max_n)
        arr = generate_test_case(n, max_val)
        
        # Run both solutions
        start_time = time.time()
        optimal_result = optimal_solution(arr, n)
        optimal_time = time.time() - start_time
        
        start_time = time.time()
        brute_force_result = brute_force_solution(arr, n)
        brute_force_time = time.time() - start_time
        
        # Compare results
        if optimal_result == brute_force_result:
            result = "PASS"
        else:
            result = "FAIL"
            
        print(f"Test #{test_num}: {result} | n={n} | Optimal: {optimal_result} ({optimal_time:.6f}s) | Brute Force: {brute_force_result} ({brute_force_time:.6f}s)")
        
        if result == "FAIL":
            print(f"Input array: {arr}")
            print("This is a failing test case!")
            return False
    
    print(f"All {num_tests} tests passed!")
    return True

def test_specific_cases():
    """Test some specific edge cases"""
    test_cases = [
        # Edge cases
        [1],                      # Single element
        [1, 1],                   # Two identical elements
        [1, 2, 3, 4, 5],          # All unique
        [10, 10, 10, 10, 10],     # All identical
        [1024, 1024, 512, 512, 256, 256, 128, 128],  # Powers of 2
        [999999999, 999999999],   # Large identical numbers
        [0, 0, 0],                # All zeros
        
        # Challenging cases
        [8, 4, 2, 1],             # Already a sequence of divisions
        [7, 7, 3, 3, 1, 1],       # Odd numbers
        [10, 10, 5, 5, 2, 2, 1, 1]  # Mix of odd and even
    ]
    
    for i, test_case in enumerate(test_cases):
        n = len(test_case)
        optimal_result = optimal_solution(test_case, n)
        brute_force_result = brute_force_solution(test_case, n)
        
        if optimal_result == brute_force_result:
            result = "PASS"
        else:
            result = "FAIL"
            
        print(f"Specific Test #{i+1}: {result} | Input: {test_case} | Optimal: {optimal_result} | Brute Force: {brute_force_result}")
        
        if result == "FAIL":
            print("This is a failing test case!")
            return False
    
    return True

if __name__ == "__main__":
    print("Testing specific cases...")
    if test_specific_cases():
        print("\nRunning random tests...")
        # Start with smaller tests for quicker feedback
        run_tests(num_tests=20, max_n=20, max_val=100)
        
        # Then run larger tests
        print("\nRunning larger random tests...")
        run_tests(num_tests=10000, max_n=50, max_val=10**5)