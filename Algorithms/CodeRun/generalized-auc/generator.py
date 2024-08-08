import random

def generate_test_case(n, case_type):
    if case_type == 1:
        # Case 1: n <= 10; 0 <= t_i, y_i <= 10; t_i, y_i are integers
        t = [random.randint(0, 10) for _ in range(n)]
        y = [random.randint(0, 10) for _ in range(n)]
    elif case_type == 2:
        # Case 2: n = 1000; 0 <= t_i, y_i <= 10; t_i, y_i are integers
        t = [random.randint(0, 10) for _ in range(n)]
        y = [random.randint(0, 10) for _ in range(n)]
    elif case_type == 3:
        # Case 3: n = 10^5; 0 <= t_i, y_i <= 1; t_i, y_i are floats with up to 6 decimal places
        t = [round(random.uniform(0, 1), 6) for _ in range(n)]
        y = [round(random.uniform(0, 1), 6) for _ in range(n)]
    else:
        raise ValueError("Invalid case type")

    return n, list(zip(t, y))

n, data = generate_test_case(100_000, 3)
# save the data to 'input.txt'
with open('input.txt', 'w') as f:
    f.write(f"{n}\n")
    for t, y in data:
        f.write(f"{t} {y}\n")
