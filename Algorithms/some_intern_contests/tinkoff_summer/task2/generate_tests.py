import random

def next_train_time(a, b, arrival_time):
    if arrival_time <= a:
        return a
    last_train_time = a + ((arrival_time - a) // b) * b
    return last_train_time + b if last_train_time != arrival_time else arrival_time

def generate_test_cases_with_answers(filename="task2_cases_with_answers.txt", num_schedules=100, num_queries=1000):
    with open(filename, 'w') as f:
        # Write the number of schedules
        f.write(f"{num_schedules}\n")
        
        # Generate random schedules
        schedules = []
        for _ in range(num_schedules):
            a = random.randint(0, 10**9)
            b = random.randint(0, 10**9)
            schedules.append((a, b))
            f.write(f"{a} {b}\n")
        
        # Write the number of queries
        f.write(f"{num_queries}\n")
        
        # Generate random queries and calculate expected answers
        for _ in range(num_queries):
            t = random.randint(1, num_schedules)
            d = random.randint(1, 10**8)
            expected_answer = next_train_time(*schedules[t-1], d)
            f.write(f"{t} {d} {expected_answer}\n")

if __name__ == "__main__":
    generate_test_cases_with_answers()
    print("Test cases with answers generated and saved to task2_cases_with_answers.txt")