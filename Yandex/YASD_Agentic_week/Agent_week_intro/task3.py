def main():
    n, k = map(int, input().split())
    if k > 0:
        platforms = set(map(int, input().split()))
    else:
        input()
        platforms = set()

    platforms.add(0)
    platforms.add(n)

    INF = float('inf')

    dp_fwd = [INF] * (n + 1)
    dp_fwd[0] = 0
    for x in range(1, n + 1):
        if x not in platforms:
            continue
        if x - 1 >= 0 and dp_fwd[x - 1] < INF:
            dp_fwd[x] = min(dp_fwd[x], dp_fwd[x - 1] + 1)
        if x - 2 >= 0 and dp_fwd[x - 2] < INF:
            dp_fwd[x] = min(dp_fwd[x], dp_fwd[x - 2] + 1)

    if dp_fwd[n] == INF:
        print(-1)
        return

    dp_bwd = [INF] * (n + 1)
    dp_bwd[n] = 0
    for x in range(n - 1, -1, -1):
        if x not in platforms:
            continue
        if x + 1 <= n and dp_bwd[x + 1] < INF:
            dp_bwd[x] = min(dp_bwd[x], dp_bwd[x + 1] + 1)
        if x + 2 <= n and dp_bwd[x + 2] < INF:
            dp_bwd[x] = min(dp_bwd[x], dp_bwd[x + 2] + 1)

    print(dp_fwd[n])

    path = []
    pos = 0
    total = dp_fwd[n]
    while pos < n:
        if (pos + 1 <= n and (pos + 1) in platforms
                and dp_fwd[pos] + 1 + dp_bwd[pos + 1] == total):
            path.append('1')
            pos += 1
        elif (pos + 2 <= n and (pos + 2) in platforms
                and dp_fwd[pos] + 1 + dp_bwd[pos + 2] == total):
            path.append('2')
            pos += 2
        else:
            print(-1)
            return

    print(''.join(path))


if __name__ == "__main__":
    main()