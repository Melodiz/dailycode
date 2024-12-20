def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # backtrack
    lcs_length = dp[m][n]
    indx1, indx2 = [], []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            indx1.append(i)
            indx2.append(j)
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, indx1[::-1], indx2[::-1]


def main():
    s1 = input()
    s2 = input()
    a, b, c = longest_common_subsequence(s1, s2)
    print(a)
    print(*b)
    print(*c)


if __name__ == "__main__":
    main()
