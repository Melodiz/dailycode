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
    data = list(map(int, input().split()))
    s = sum(data)
    if s % 2 != 0:
        print("NO")
        return 0
    else:
        if min_difference(data) == 0:
            print("YES") 
        else: print("NO")

if __name__ == "__main__":
    main()

