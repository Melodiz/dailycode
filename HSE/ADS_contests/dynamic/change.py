def coin_change(nominals, target):
    dp = [target + 1] * (target + 1)
    dp[0] = 0
    
    coin_used = [0] * (target + 1)

    for i in range(1, target + 1):
        for coin in nominals:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin

    if dp[target] > target:
        return -1, []

    coins = []
    current = target
    while current > 0:
        coins.append(coin_used[current])
        current -= coin_used[current]

    return dp[target], coins

def main():
    n = int(input())
    nominals = list(map(int, input().split()))
    S = int(input())

    min_coins, coins_used = coin_change(nominals, S)

    if min_coins == -1:
        print(-1)
    else:
        print(min_coins)
        print(*coins_used)

if __name__ == "__main__":
    main()