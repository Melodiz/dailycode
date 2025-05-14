from solution import solve
import time
from tqdm import tqdm

def get_cases(filename = 'task7/7cases.txt'):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            numbers = list(map(int, line.strip().split()))
            ans = numbers[0]
            A = numbers[1:]
            data.append((ans, A))
    return data

def run_test():
    avarage_time = 0
    worst_time = 0
    for ans, A in tqdm(get_cases()):
        start_time = time.time()
        result = solve(A)
        end_time = time.time()
        avarage_time += end_time - start_time
        worst_time = max(worst_time, end_time - start_time)
        assert result == ans, f"Test failed for ans={ans}, A={A}, result={result}"
    print(f"Average time taken: {avarage_time / len(get_cases())} seconds")
    print(f"Worst time taken: {worst_time} seconds")

if __name__ == "__main__":
    run_test()


