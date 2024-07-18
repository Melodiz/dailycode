def hanoi_4_pegs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Find the optimal k
    min_steps = float('inf')
    k = 0
    for k in range(1, n):
        steps = 2 * hanoi_4_pegs(k) + hanoi_3_pegs(n - k)
        if steps < min_steps:
            min_steps = steps
            k = k

    return 2 * hanoi_4_pegs(k) + hanoi_3_pegs(n - k)


def hanoi_3_pegs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * hanoi_3_pegs(n-1) + 1


n = int(input())
print(hanoi_4_pegs(n))
