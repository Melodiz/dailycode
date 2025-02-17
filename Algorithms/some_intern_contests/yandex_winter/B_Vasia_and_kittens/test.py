import random
# from brute_bin import find_max_window_size
from resulting_solution import solve
from naive_brute import naive_brute_force
from tqdm import tqdm

def generate_test_case(max_m=15, max_coordinate=100):
    n = random.randint(2, max_m - 1)
    m = random.randint(n + 1, max_m)
    k = random.randint(0, (n - 1))
    
    places = sorted(random.sample(range(1, max_coordinate + 1), m))
    taken_places = random.sample(places, k) if k > 0 else []
    
    return n, m, k, places, taken_places

def run_tests(num_tests=1000):
    for i in tqdm(range(num_tests)):
        n, m, k, places, taken_places = generate_test_case()
        
        optimized_result = solve(n, m, k, places, taken_places)
        naive_result = naive_brute_force(places, n, taken_places)
        
        if optimized_result != naive_result:
            print("Test case FAILED!")
            print(f"Test case {i + 1}:")
            print(n, m, k)
            print(' '.join(map(str, places)))
            print(' '.join(map(str, taken_places)))
            print(f"Optimized result: {optimized_result}")
            print(f"Naive brute force result: {naive_result}")
            return False
        
    
    print("All tests passed!")
    return True

if __name__ == "__main__":
    run_tests()