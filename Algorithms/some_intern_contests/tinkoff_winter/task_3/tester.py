import random
import time
from brute import solve_brute
from solution import min_operations_to_adjust_range
from tqdm import tqdm
def generate_test_case(n, max_val):
    A = [random.randint(1, max_val) for _ in range(n)]
    m = random.randint(1, n-2)
    l = random.randint(1, max_val)
    h = random.randint(1, max_val)
    return A, m, l, h

def test_solutions(num_tests, max_n, max_val):
    total_brute_time = 0
    total_optimized_time = 0

    for test in tqdm(range(num_tests)):
        n = random.randint(3, max_n)
        A, m, l, h = generate_test_case(n, max_val)
        
        start_time = time.time()
        brute_force_result = solve_brute(A, m, l, h)
        brute_time = time.time() - start_time
        total_brute_time += brute_time

        start_time = time.time()
        optimized_result = min_operations_to_adjust_range(A, m, l, h)
        optimized_time = time.time() - start_time
        total_optimized_time += optimized_time
        
        if brute_force_result != optimized_result:
            print(f"Test case {test + 1} failed:")
            print(f"Brute force result: {brute_force_result}")
            print(f"Optimized result: {optimized_result}")
            print(n, m)
            print(*([l, h] + A), '\n')
            return False
    
    print("All test cases passed!")
    print(f"Average brute force time: {total_brute_time/num_tests:.6f} seconds")
    print(f"Average optimized time: {total_optimized_time/num_tests:.6f} seconds")
    return True

def test_max_input():
    max_n = 2 * 10**5
    max_val = 10**9  # Assuming this as the maximum value for array elements, l, and h
    
    A = [random.randint(1, max_val) for _ in range(max_n)]
    m = max_n - 2  # Maximum possible m
    l = random.randint(1, max_val)
    h = random.randint(1, max_val)

    print("Testing with maximum input:")
    print(f"n = {max_n}, m = {m}")
    print(f"l = {l}, h = {h}")
    print("First few elements of A:", A[:10])

    start_time = time.time()
    result = min_operations_to_adjust_range(A, m, l, h)
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    num_tests = 100
    max_n = 200  # Keeping this small for brute-force to finish in reasonable time
    max_val = 100
    test_solutions(num_tests, max_n, max_val)

    print("\nTesting with maximum possible input:")
    test_max_input()