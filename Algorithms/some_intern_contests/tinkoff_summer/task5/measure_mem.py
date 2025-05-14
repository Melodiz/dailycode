from memory_profiler import profile
from solution import optimal_solution
import random
@profile
def test_optimal_solution():
    # Example of an extreme case
    n = 500_000
    a = random.randint(1, 10) 
    b = random.randint(1, 10) 
    s = ''.join([random.choice(['(', ')']) for _ in range(2*n)])

    result = optimal_solution(s, a, b)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_optimal_solution()