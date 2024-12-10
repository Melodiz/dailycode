def toll_stairs(data):
    n = len(data)
    if n == 1:
        return data[0]
    
    dp = [0] * n
    dp[0] = data[0]
    dp[1] = data[1]
    
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + data[i]
    
    return dp[-1]

def main():
    n = int(input())
    data = list(map(int, input().split()))
    print(toll_stairs(data))

if __name__ == "__main__":
    main()