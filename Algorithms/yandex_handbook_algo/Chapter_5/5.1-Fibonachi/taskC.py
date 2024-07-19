def calc_Pisano_period(m):
    current = 0
    next = 1
    for period in range(0, m * m):
        current, next = next, (current + next) % m
        if current == 0 and next == 1:
            return period + 1

def fibonacci_mod_m(n, m):
    cycle_length = calc_Pisano_period(m)
    n = n % cycle_length

    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

n, m = map(int, input().split())
print(fibonacci_mod_m(n, m))