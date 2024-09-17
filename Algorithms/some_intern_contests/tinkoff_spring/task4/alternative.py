from math import isqrt

def sieve_eratosthenes(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for start in range(3, isqrt(n) + 1, 2):
        if sieve[start]:
            for multiple in range(start * start, n + 1, start * 2):
                sieve[multiple] = False
    return [2] + [num for num in range(3, n + 1, 2) if sieve[num]]

def solution(L, R):
    primes = sieve_eratosthenes(isqrt(R) + 10)
    primes_set = set(primes[1:])  # Exclude the first prime (2) from the set
    counter = 0
    for p in primes:
        q = 2
        num = p
        while num <= R:
            if num >= L and q in primes_set:
                counter += 1
            num *= p
            q += 1
    return counter

def main():
    L, R = list(map(int, input().split()))
    # L, R = 1, 10**14  # Example input for testing
    print(solution(L, R))
    return 0

if __name__ == "__main__":
    main()