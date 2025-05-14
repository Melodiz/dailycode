import random
from collections import Counter

def main(arr):
    arr.sort(reverse=True)
    unique = set(arr)
    cnt = Counter(arr)
    for i in range(len(arr)):
        if cnt[arr[i]] == 1:
            continue
        cnt[arr[i]] -= 1
        while arr[i] in unique and arr[i] > 0:
            arr[i] //= 2
        unique.add(arr[i])
    return len(set(arr))

def generate_test_cases_with_answers(filename="3cases.txt", num_cases=10, max_n=2*10**5, max_value=10**9):
    with open(filename, 'w') as f:
        for _ in range(num_cases):
            n = random.randint(1, max_n)
            arr = [random.randint(1, max_value) for _ in range(n)]
            expected_answer = main(arr.copy())
            f.write(f"{n}\n")
            f.write(" ".join(map(str, arr)) + "\n")
            f.write(f"{expected_answer}\n")

if __name__ == "__main__":
    generate_test_cases_with_answers()
    print("Test cases with answers generated and saved to task3_cases_with_answers.txt")