import time
import random
from solution import optimal_solution
from tqdm import tqdm

def read_cases(filename):
    with open(filename, 'r') as f:
        cases = []
        for line in f:
            n, a, b, s, ans = line.strip().split()
            cases.append((int(n), int(a), int(b), s, int(ans)))
    return cases

def test_solution_and_performance():
    # small test cases for correctness
    with open('task5/5_cases.txt', 'r') as f:
        for line in f:
            s, a, b, ans = line.strip().split()
            assert optimal_solution(s, int(a), int(b)) == int(ans)
    print("All small test cases passed!")

    # large test cases for performance
    large_cases = read_cases('task5/5_test.txt')
    avarage_time = 0
    worst_time = 0
    for n, a, b, s, ans in tqdm(large_cases):
        start_time = time.time()
        assert optimal_solution(s, a, b) == ans
        end_time = time.time()
        execution_time = end_time - start_time
        if execution_time > worst_time:
            worst_time = execution_time
        avarage_time += execution_time
    print(f"Average execution time: {(avarage_time / len(large_cases)):2f} seconds")
    print(f"Worst execution time: {(worst_time):2f} seconds")


if __name__ == "__main__":
    test_solution_and_performance()

# Average execution time: 0.002027 seconds
# Worst execution time: 0.002322 seconds