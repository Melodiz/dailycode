import re

def prefix_function(text):
    n = len(text)
    p = [0] * n
    for i in range(1, n):
        if text[p[i - 1]] == text[i]:
            p[i] = p[i - 1] + 1
        else:
            j = p[i - 1]
            while j > 0 and text[i] != text[j]:
                j = p[j - 1]
            if text[i] == text[j]:
                j += 1
            p[i] = j
    return p

def KMP(text, pattern):
    concat = pattern + '$' + text
    p_values = prefix_function(concat)
    result = []
    for i in range(len(concat)):
        if p_values[i] == len(pattern):
            result.append(i - 2 * len(pattern))
    return result  # Add this return statement

def brute(text, pattern):
    return [m.start() for m in re.finditer(pattern, text)]

def test():
    import random
    for _ in range(1000):
        text = ''.join(random.choices('abcdefg', k=10_000))
        pattern = ''.join(random.choices('abcdefg', k=7))
        assert KMP(text, pattern) == brute(text, pattern)
    print("All tests passed!")

if __name__ == "__main__":
    test()