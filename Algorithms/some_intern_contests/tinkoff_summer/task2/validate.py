import time

def next_train_time(a, b, arrival_time):
    if arrival_time <= a:
        return a
    last_train_time = a + ((arrival_time - a) // b) * b
    return last_train_time + b if last_train_time != arrival_time else arrival_time

def read_test_cases(filename="task2_cases_with_answers.txt"):
    with open(filename, 'r') as f:
        num_schedules = int(f.readline().strip())
        schedules = [tuple(map(int, f.readline().strip().split())) for _ in range(num_schedules)]
        num_queries = int(f.readline().strip())
        queries = [tuple(map(int, f.readline().strip().split())) for _ in range(num_queries)]
    return schedules, queries

def test_solution():
    schedules, queries = read_test_cases()
    total_time = 0
    worst_time = 0
    num_queries = len(queries)

    for t, d, expected_answer in queries:
        a, b = schedules[t-1]
        start_time = time.perf_counter()
        result = next_train_time(a, b, d)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        total_time += execution_time
        worst_time = max(worst_time, execution_time)
        
        assert result == expected_answer, f"Test failed for t={t}, d={d}, expected={expected_answer}, got={result}"

    average_time = total_time / num_queries
    print(f"Average execution time: {average_time:.6f} seconds")
    print(f"Worst execution time: {worst_time:.6f} seconds")

if __name__ == "__main__":
    test_solution()