from memory_profiler import profile
from solution import solve
import random

@profile
def test_solve_memory():
    # Create a large test case
    n = 10**5  # Maximum size according to problem constraints
    arr = [random.randint(1, 10) for _ in range(n)]
    
    # Run the solution
    result = solve(arr)
    return result

if __name__ == "__main__":
    test_solve_memory()