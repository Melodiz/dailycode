def knapsack_with_path(weights, values, capacity, n):

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1]
                               [w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacity
    path = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            path.append(i)
            w -= weights[i-1]

    return path[::-1]


def main():
    n, capacity = map(int, input().split())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    
    path = knapsack_with_path(weights, values, capacity, n)
    for i in path:
        print(i)

    return 0


if __name__ == '__main__':
    main()
