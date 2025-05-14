def is_almost_palindrome(s):
    for miss_index in range(len(s)):
        new_s = s[:miss_index] + s[miss_index + 1:]
        if new_s == new_s[::-1]:
            return 'YES'
    return 'NO'

def generate_test_cases_with_answers(filename="task1_cases_with_answers.txt", num_cases=100_000):
    import random
    import string

    with open(filename, 'w') as f:
        for _ in range(num_cases):
            # Generate a random string of length up to 4
            length = 4
            s = ''.join(random.choices(string.ascii_lowercase, k=length))
            expected_answer = is_almost_palindrome(s)
            f.write(f"{s}\n")
            f.write(f"{expected_answer}\n")

if __name__ == "__main__":
    generate_test_cases_with_answers()
    print("Test cases with answers generated and saved to task1_cases_with_answers.txt")