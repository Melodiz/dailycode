from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_mod_10(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_mod_10(n-1) + fibonacci_mod_10(n-2)) % 10


def fibonacci_sum_last_digit(n):
    return (fibonacci_mod_10((n+2) % 60) - 1) % 10


def fibonacci_partial_sum_last_digit(n, m):
    # calculate the last digit of the sum of fibonacci numbers from m to n
    if m < n:
        return (fibonacci_sum_last_digit(n) - fibonacci_sum_last_digit(m-1)) % 10
    return fibonacci_mod_10(m % 60)


n, m = map(int, input().split())
print(fibonacci_partial_sum_last_digit(n, m))
