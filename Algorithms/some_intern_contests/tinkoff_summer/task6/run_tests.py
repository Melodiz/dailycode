from solution import smart
from tqdm import tqdm
import time
import random

def get_tests(filename = 'task6/6_casesLARGE.txt'):
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            n = int(lines[i].strip())
            heights = list(map(int, lines[i+1].strip().split()))
            expected_output = int(lines[i+2].strip())
            data.append((n, heights, expected_output))
    data.sort(key=lambda x: x[0])
    return data

def main(with_large=False):
    data = get_tests()
    total_time = 0
    worst_time = 0
    for n, heights, expected_output in tqdm(data):
        start_time = time.time()
        result = smart(heights)
        assert result == expected_output, f"Test failed for n={n}, heights={heights}, expected_output={expected_output}, result={result}  \n"
        end_time = time.time()
        total_time += end_time - start_time
        worst_time = max(worst_time, end_time - start_time)
    print(f"Average time taken: {total_time / len(data)} seconds")
    print(f"Worst time taken: {worst_time} seconds")

    # test on large test case
    if not with_large: return 
    n = [100, 10**3, 10**4, 10**5, 3*10**5]
    for i in n:
        large_avg = 0
        large_worst = 0
        for t in range(3):
            heights = [random.randint(1, 1000) for _ in range(i+1)]
            start_time = time.time()
            result = smart(heights)
            end_time = time.time()
            large_avg += end_time - start_time
            large_worst = max(large_worst, end_time - start_time)
        print(f"Large test case {i}, average time taken: {large_avg / 3} seconds, worst time taken: {large_worst} seconds")

if __name__ == "__main__":
    main(1)