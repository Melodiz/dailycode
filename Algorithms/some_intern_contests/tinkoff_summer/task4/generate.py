from bruteforce import brute
import random
from tqdm import tqdm

def generate_cases(num_cases=100_000, min_size=3, max_size=100):
    # test_cases = []
    with open('task4/4cases.txt', 'w') as f:
        for _ in tqdm(range(num_cases)):
            size = random.randint(min_size, max_size)
            arr = [random.randint(1, 10) for _ in range(size)]
            ans = brute(arr)
            # test_cases.append((arr, ans))
            f.write(f'{size} {ans} {" ".join(map(str, arr))}\n')
    # return test_cases

if __name__ == "__main__":
    generate_cases()