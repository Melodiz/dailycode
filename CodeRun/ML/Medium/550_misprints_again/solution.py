def diagonal_levenshtein(s1, s2, k):
    len_s1, len_s2 = len(s1), len(s2)
    
    # If the length difference is greater than k, return a large number
    if abs(len_s1 - len_s2) > k:
        return float('inf')
    
    # Initialize the distance matrix
    dp = [[float('inf')] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
    # Set the initial values for the first row and column
    for i in range(len_s1 + 1):
        dp[i][0] = i
    for j in range(len_s2 + 1):
        dp[0][j] = j
    
    # Fill the distance matrix within the band of width 2k + 1
    for i in range(1, len_s1 + 1):
        for j in range(max(1, i - k), min(len_s2, i + k) + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
    
    # Return the Levenshtein distance
    return dp[len_s1][len_s2]

def main():
    for _ in range(int(input())):
        k, s1, s2 = int(input()), input().strip(), input().strip()
        print('Yes' if diagonal_levenshtein(s1, s2, k)<=k else 'No')

if __name__ == '__main__':
    main()
    

