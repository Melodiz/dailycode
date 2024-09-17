from math import isqrt

def sieve_eratosthenes(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for start in range(3, isqrt(n) + 1, 2):
        if sieve[start]:
            for multiple in range(start*start, n + 1, start*2):
                sieve[multiple] = False
    return [2] + [num for num in range(3, n + 1, 2) if sieve[num]]


def solution(L, R):
    primes = sieve_eratosthenes(isqrt(R)+1)
    primes_set = set(primes[1:])
    nums = []
    counter = 0
    for p in primes:
        q = 2
        num = pow(p, q-1)
        while num <= R:
            if num >= L and q in primes_set:
                counter += 1
                nums.append(num)
            num *= p
            q += 1
    return counter


def main():
    L, R = list(map(int, input().split()))
    print(solution(L, R))
    return 0


if __name__ == "__main__":
    main()

# the only way left to optimize this solution is to optimize the sieve algorithm,
# 'cause the solution is already takes no more than 0.1 s
