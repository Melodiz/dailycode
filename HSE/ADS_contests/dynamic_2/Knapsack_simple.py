def knapsack(weights, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + weights[i])

    return dp[capacity]

def main():
    S, N = map(int, input().split())
    weights = list(map(int, input().split()))
    
    max_weight = knapsack(weights, S)
    print(max_weight)

if __name__ == "__main__":
    main()