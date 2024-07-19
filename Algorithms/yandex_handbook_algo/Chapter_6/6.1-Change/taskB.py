def change(n):
    nominals = [1, 5, 10, 20, 50]
    coins = [0] * len(nominals)
    for i in range(len(nominals)-1, -1, -1):
        coins[i] = n // nominals[i]
        n %= nominals[i]
    return coins


def print_change(coins):
    ans = '50 ' * coins[4] + '20 ' * coins[3] + \
        '10 '*coins[2] + '5 '*coins[1] + '1 '*coins[0]
    print(ans.rstrip())

n = int(input())
coins = change(n)
print(sum(coins))
print_change(coins)
