def main():
    k, s, t = int(input()), input(), input()
    if k > len(s) or k > len(t):
        return False
    
    friend_pool = [0] * 26
    for char in t:
        friend_pool[ord(char) - 97] += 1

    window_cnt = [0] * 26
    for i in range(k):
        window_cnt[ord(s[i]) - 97] += 1

    matches = 0
    for i in range(26):
        if window_cnt[i] <= friend_pool[i]:
            matches += 1

    if matches == 26:
        return True

    for i in range(k, len(s)):
        char_out = ord(s[i-k]) - 97
        was_matching_out = window_cnt[char_out] <= friend_pool[char_out]
        window_cnt[char_out] -= 1
        is_matching_out = window_cnt[char_out] <= friend_pool[char_out]
        
        if not was_matching_out and is_matching_out: matches += 1
        elif was_matching_out and not is_matching_out: matches -= 1

        char_in = ord(s[i]) - 97
        was_matching_in = window_cnt[char_in] <= friend_pool[char_in]
        window_cnt[char_in] += 1
        is_matching_in = window_cnt[char_in] <= friend_pool[char_in]

        if not was_matching_in and is_matching_in: matches += 1
        elif was_matching_in and not is_matching_in: matches -= 1

        if matches == 26:
            return True

    return False

if __name__ == "__main__":
    print("YES" if main() else "NO")