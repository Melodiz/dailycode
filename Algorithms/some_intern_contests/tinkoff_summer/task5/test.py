import time
import statistics
from typing import Tuple, List
from solution import optimal_solution

def read_test_cases(filename: str) -> List[Tuple[str, int, int, Tuple[int, int]]]:
    """
    Read test cases from the specified file.
    
    Args:
        filename: Path to the test cases file
        
    Returns:
        List of tuples (s, a, b, expected_result)
    """
    test_cases = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 4:
                s = parts[0]
                a = int(parts[1])
                b = int(parts[2])
                expected = tuple(map(int, parts[3].split(',')))
                test_cases.append((s, a, b, expected))
    return test_cases

def run_tests(test_cases: List[Tuple[str, int, int, Tuple[int, int]]], num_iterations: int = 100) -> None:
    """
    Run tests on the solution function and measure execution time.
    
    Args:
        test_cases: List of test cases
        num_iterations: Number of iterations for timing measurements
    """
    print(f"Running {len(test_cases)} test cases, {num_iterations} iterations each")
    print("-" * 60)
    
    all_times = []
    worst_case_time = 0
    worst_case_input = None
    
    # Test correctness and measure time
    for i, (s, a, b, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: s='{s}', a={a}, b={b}")
    
        # Measure execution time
        times = []
        for _ in range(num_iterations):
            start_time = time.perf_counter()
            optimal_solution(s, a, b)
            end_time = time.perf_counter()
            execution_time = (end_time - start_time) * 1_000_000  # Convert to microseconds
            times.append(execution_time)
            all_times.append(execution_time)
            
            # Track worst case
            if execution_time > worst_case_time:
                worst_case_time = execution_time
                worst_case_input = (s, a, b)
        
        avg_time = statistics.mean(times)
        print(f"  Average execution time: {avg_time:.2f} microseconds")
        print("-" * 60)
    
    # Print overall statistics
    overall_avg_time = statistics.mean(all_times)
    worst_case_time = worst_case_time / 1_000_000  # Convert to seconds
    print(f"Overall average execution time: {overall_avg_time:.2f} microseconds")
    print(f"Worst case execution time: {worst_case_time:.2f} seconds")
    print(f"Worst case input: s='{worst_case_input[0]}', a={worst_case_input[1]}, b={worst_case_input[2]}")

if __name__ == "__main__":
    try:
        test_cases = read_test_cases("5_cases.txt")
        if test_cases:
            run_tests(test_cases)
        else:
            print("No test cases found in 5_cases.txt")
    except FileNotFoundError:
        print("Error: File '5_cases.txt' not found.")
    except Exception as e:
        print(f"Error: {e}")