import sympy
from tqdm import tqdm
import random
from joblib import Parallel, delayed

def save_results(results):
    with open("task4/results.txt", "w") as f:
        for L, R, value in results:
            f.write(f"{L} {R} {value}\n")

def bruteforce(L, R):
    counter = 0
    for p in range(L, R+1):
        if not sympy.isprime(p):
            if sympy.isprime(sympy.divisor_count(p)):
                counter += 1
    return counter

def generate():
    num_jobs = -1  # Use all available CPU cores
    tasks = [(random.randint(0, R), R) for R in [random.randint(5, 10**6) for _ in range(100)]]
    
    results = Parallel(n_jobs=num_jobs)(delayed(bruteforce)(L, R) for L, R in tqdm(tasks))
    
    result = [(L, R, value) for (L, R), value in zip(tasks, results)]
    save_results(result)

def read_data():
    with open("task4/results.txt", "r") as f:
        return [(int(line.split()[0]), int(line.split()[1]), int(line.split()[2])) for line in f]
    

def factorSolution(L, R):
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def factor(n):
        # return the amout of factors of n
        if n == 1: return 1
        if n == 2: return 2
        if n == 0: return 0
        if n == 3: return 2
        return 

def main():
    test_cases = read_data()
    for L, R, expected in test_cases:
        assert bruteforce(L, R) == expected, f"Expected {expected} for {L}-{R}, but got {bruteforce(L, R)}"
        print("Test case passed")

if __name__ == "__main__":
    # main()
    factorSolution(10, 20)