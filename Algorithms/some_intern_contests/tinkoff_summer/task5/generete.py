import sys
from collections import deque
from itertools import product
from tqdm import tqdm
import random
from solution import optimal_solution


def create_test_cases():
    with open("5_cases_large.txt", "w") as f:
        for _ in tqdm(range(500)):
            n = 10**5
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            s = ''.join(random.choice('()') for _ in range(2*n))
            answer = optimal_solution(s, a, b)
            f.write(f"{n} {a} {b} {s} {answer}\n")
    print("Test cases created successfully.")

if __name__ == "__main__":
    create_test_cases()