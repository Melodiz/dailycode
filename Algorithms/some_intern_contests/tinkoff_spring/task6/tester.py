from solution import find_min_time
from tqdm import tqdm
import time

def tester():
    with open("test_cases.txt", "r") as file:
        lines = file.readlines()
    
    i = 0
    total_tests = 0
    while i < len(lines):
        n = int(lines[i].strip())
        i += 1 + n + 1  # Skip over the processes and the expected min time
        total_tests += 1
    
    total_time = 0
    max_time = 0
    with tqdm(total=total_tests, desc="Running tests") as pbar:
        with open("worst_case.txt", "r") as file:
            while True:
                n_line = file.readline()
                if not n_line:
                    break
                n = int(n_line.strip())
                processes = []
                for _ in range(n):
                    process_data = list(map(int, file.readline().strip().split()))
                    processes.append(process_data)
                expected_min_time = int(file.readline().strip())
                
                start_time = time.time()
                print('start')
                calculated_min_time = find_min_time(n, processes)
                end_time = time.time()
                
                assert calculated_min_time == expected_min_time, f"Test failed: expected {expected_min_time}, got {calculated_min_time}"
                pbar.update(1)
                
                elapsed_time = end_time - start_time
                total_time += elapsed_time
                if elapsed_time > max_time: 
                    max_time = elapsed_time
    
    avg_time = total_time / total_tests
    print(f"All tests passed. Average time per test: {avg_time:.4f} seconds.")
    print(f"Worst case time: {max_time:.4f} seconds.")

# Run the tester function
tester()