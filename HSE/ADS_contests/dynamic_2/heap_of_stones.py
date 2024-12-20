def min_difference(weights):
    ans = sum(weights)
    target = ans // 2
    n = len(weights)
    
    dp = [False] * (target + 1)
    dp[0] = True
    
    for weight in weights:
        for j in range(target, weight - 1, -1):
            dp[j] |= dp[j - weight]
    
    for j in range(target, -1, -1):
        if dp[j]:
            return ans - 2 * j

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    
    result = min_difference(weights)
    print(result)

if __name__ == "__main__":
    main()