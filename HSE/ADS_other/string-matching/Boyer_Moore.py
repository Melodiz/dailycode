import random
import re

def bad_character_rule(pattern, char, index):
    last_occurrence = -1
    for i in range(index - 1, -1, -1):
        if pattern[i] == char:
            last_occurrence = i
            break
    if last_occurrence == -1:
        return index + 1
    return index - last_occurrence

def z_function(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        if i > right:
            left, right = i, i
            while right < len(s) and s[right] == s[right - left]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < len(s) and s[right] == s[right - left]:
                    right += 1
                z[i] = right - left
                right -= 1
    return z

def good_suffix_rule(pattern):
    pattern_length = len(pattern)
    reversed_pattern = pattern[::-1]
    z = z_function(reversed_pattern)
    good_suffix_shift = [pattern_length] * (pattern_length + 1)

    for i in range(pattern_length - 1):
        j = pattern_length - z[i] - 1
        good_suffix_shift[j] = min(good_suffix_shift[j], i + 1)

    last_prefix_position = pattern_length
    for i in range(pattern_length):
        if i + z[i] == pattern_length:
            last_prefix_position = i
        good_suffix_shift[pattern_length - i - 1] = min(good_suffix_shift[pattern_length - i - 1], last_prefix_position + pattern_length - i - 1)

    return good_suffix_shift

def boyer_moore(text, pattern):
    pattern_length = len(pattern)
    text_length = len(text)
    if pattern_length == 0:
        return []

    bad_char_shift = {char: bad_character_rule(pattern, char, pattern_length) for char in set(pattern)}
    good_suffix_shift = good_suffix_rule(pattern)

    matches = []
    s = 0
    while s <= text_length - pattern_length:
        j = pattern_length - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            matches.append(s)
            s += good_suffix_shift[0] if pattern_length < text_length else 1
        else:
            bad_char_shift_value = bad_char_shift.get(text[s + j], pattern_length)
            good_suffix_shift_value = good_suffix_shift[j + 1]
            s += max(1, j - bad_char_shift_value, good_suffix_shift_value)

    return matches

def brute(text, pattern):
    return [m.start() for m in re.finditer(pattern, text)]

def test():
    for _ in range(1000):
        text = ''.join(random.choices('abcdefg', k=10_000))
        pattern = ''.join(random.choices('abcdefg', k=7))
        assert boyer_moore(text, pattern) == brute(text, pattern)
    print("All tests passed!")

if __name__ == "__main__":
    print(boyer_moore("test test test test", "test"))
    # test()