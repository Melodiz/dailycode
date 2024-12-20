def knapsack(weights, values, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

def main():
    n, capacity = map(int, input().split())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))

    max_value = knapsack(weights, values, capacity, n)
    print(max_value)

    return 0


if __name__ == '__main__':
    main()