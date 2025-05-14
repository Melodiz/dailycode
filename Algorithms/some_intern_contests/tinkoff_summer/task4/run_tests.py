from solution import solve
# from bruteforce import brute 
import time
from statistics import mean
import sys
from tqdm import tqdm

def validate_cases(file_path='task4/4cases.txt', max_cases=None):
    print(f"Reading test cases from {file_path}...")
    
    execution_times = []
    max_time = 0
    max_time_case = None
    total_cases = 0
    correct_cases = 0
    
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
        if max_cases is not None:
            lines = lines[:max_cases]

        lines.sort(key=lambda x: int(x.split()[0]))

        for i, line in enumerate(tqdm(lines)):
            parts = line.strip().split()
            size = int(parts[0])
            expected_ans = int(parts[1])
            arr = list(map(int, parts[2:]))
            
            # Measure execution time
            start_time = time.time()
            result = solve(arr)
            end_time = time.time()
            
            execution_time = end_time - start_time
            execution_times.append(execution_time)
            
            # Track worst case
            if execution_time > max_time:
                max_time = execution_time
                max_time_case = (i, arr, expected_ans, result)
            
            # Check correctness
            total_cases += 1
            if result == expected_ans:
                correct_cases += 1
            else:
                print(f"Case {i} failed: Expected {expected_ans}, got {result}")
                print(f"Array: {arr}")
                
        # Calculate statistics
        avg_time = mean(execution_times)
        accuracy = (correct_cases / total_cases) * 100 if total_cases > 0 else 0
        
        print("\n===== Results =====")
        print(f"Total cases tested: {total_cases}")
        print(f"Correct cases: {correct_cases} ({accuracy:.2f}%)")
        print(f"Average execution time: {avg_time:.6f} seconds")
        print(f"Worst execution time: {max_time:.6f} seconds")
        
        if max_time_case:
            print(f"Worst case details:")
            print(f"  Case index: {max_time_case[0]}")
            # print(f"  Array: {max_time_case[1]}")
            print(f"  Expected answer: {max_time_case[2]}")
            print(f"  Actual answer: {max_time_case[3]}")
            
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error during validation: {e}")

from tqdm import tqdm
import random

def generate_maximal_test_case(n=10**5, max_value=10):
    """Generate an array of length n with all elements set to max_value."""
    return [random.randint(1, max_value) for _ in range(n)]

def run_maximal_test_case(iterations=50):
    with open('4large.txt', 'w') as f:
        for _ in tqdm(range(iterations)):
            arr = generate_maximal_test_case()
            ans = solve(arr)
            f.write(f"{len(arr)} {ans} {' '.join(map(str, arr))}\n")
    print("Maximal test case generated and saved to 4large.txt")

if __name__ == "__main__":
    # Parse command line arguments
    file_path = 'task4/4cases.txt'
    max_cases = 100
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    if len(sys.argv) > 2:
        try:
            max_cases = int(sys.argv[2])
        except ValueError:
            print(f"Warning: Invalid max_cases value '{sys.argv[2]}'. Using all cases.")
    
    validate_cases(file_path, max_cases)
    run_maximal_test_case()