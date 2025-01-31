import random
import time
import io
import sys

from task_7.solution import solve
def generate_test_case(n_min=3, n_max=2*10**5, k_max=299, a_max=10**8):
    n = random.randint(n_min, n_max)
    k = random.randint(1, k_max)
    a = [random.randint(1, a_max) for _ in range(n)]
    return n, k, a

def run_test_case(n, k, a):
    # Redirect stdin and stdout
    sys.stdin = io.StringIO(f"{n} {k}\n{' '.join(map(str, a))}")
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Measure execution time
    start_time = time.time()
    solve()
    end_time = time.time()

    # Restore stdin and stdout
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

    execution_time = end_time - start_time
    output = captured_output.getvalue().strip().split('\n')
    return execution_time, output

def test_solve_with_random_cases(num_tests=10):
    for i in range(num_tests):
        n, k, a = generate_test_case()
        print(f"Test case {i+1}:")
        print(f"n = {n}, k = {k}")
        print(f"First few elements of a: {a[:5]}...")
        
        execution_time, output = run_test_case(n, k, a)
        
        print(f"Execution time: {execution_time:.6f} seconds")
        print(f"First few output values: {output[:5]}...")
        print()

if __name__ == "__main__":
    test_solve_with_random_cases()
    # solve()  # Uncomment this line when submitting the solution