import time
import random
from task_4.solution import opt_solution
def generate_max_input():
    n = 2 * 10**6  # Maximum n
    x, y, z = random.randint(2, 10**6), random.randint(2, 10**6), random.randint(2, 10**6)
    a = [random.randint(1, 10**18) for _ in range(n)]
    return n, x, y, z, a

def test_max_input():
    n, x, y, z, a = generate_max_input()
    
    print(f"Testing with maximum input:")
    print(f"n = {n}, x = {x}, y = {y}, z = {z}")
    print(f"First few elements of a: {a[:5]}...")
    
    start_time = time.time()

    result = opt_solution(n, x, y, z, a)
    
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"\nResult: {result}")
    print(f"Execution time: {execution_time:.6f} seconds")

if __name__ == "__main__":
    test_max_input()