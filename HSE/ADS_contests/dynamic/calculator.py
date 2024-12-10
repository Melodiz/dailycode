def calculate(n):
    dp = [float('inf')] * (n + 1)
    history = [0] * (n + 1)
    
    dp[1] = 0
    
    for i in range(2, n + 1):
        if dp[i-1] + 1 < dp[i]:
            dp[i] = dp[i-1] + 1
            history[i] = i - 1
        
        if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i//2] + 1
            history[i] = i // 2
        
        if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
            history[i] = i // 3
    
    path = []
    current = n
    while current > 0:
        path.append(current)
        current = history[current]
    
    return dp[n], path[::-1]

def main():
    n = int(input())
    ops, path = calculate(n)
    print(ops)
    print(*path)

if __name__ == "__main__":
    main()