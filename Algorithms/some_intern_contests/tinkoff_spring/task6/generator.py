from solution import *
import random
from tqdm import tqdm
from joblib import Parallel, delayed

def generate_random_test_cases(num_test_cases=100, max_n=10**4):
    with open("test_cases.txt", "w") as file:
        for test_n_iteration in tqdm(range(num_test_cases), desc="Generating test cases"):
            if test_n_iteration >= num_test_cases - 2:
                n = 10**5
            else:
                n = random.randint(1, max_n)
            processes = []
            used = set()
            for i in range(n):
                t_i = random.randint(0, 10**12)
                dependencies = random.sample(range(1, n+1), min(random.randint(0, n-1), 30))
                dependencies = [dep for dep in dependencies if dep != i+1 and dep not in used]  # Avoid self-dependency
                processes.append([t_i] + dependencies)
                used.update(dependencies)
            file.write(f"{n}\n")
            for process in processes:
                file.write(' '.join(map(str, process)) + '\n')
            min_time = find_min_time(n, processes)
            file.write(f"{min_time}\n")

# Generate test cases
generate_random_test_cases()

# with open("worst_case.txt", "w") as f:
#     f.write("10000\n")
#     for i in range(10 ** 4):
#         f.write(f"{str(i + 1)} ")
#         for j in range(i + 1, 10 ** 4):
#             f.write(f"{str(j + 1)} ")
#         f.write("\n")