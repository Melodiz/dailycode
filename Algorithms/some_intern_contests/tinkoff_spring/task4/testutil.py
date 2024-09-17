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
    counter = 0
    for p in primes:
        q = 2
        num = pow(p, q-1)
        while num <= R:
            if num >= L and q in primes_set:
                counter += 1
            num *= p
            q += 1
    return counter


def test():
    cases = [(1, 10), (1, 10**2), (1, 10**3), (1, 10**4), (1, 10**5), (1, 412441),
             (1, 414152), (1, 41_252), (1, 19121), (1, 4124), (1, 415), (1, 3), (1, 2)]
    expected = [2, 7, 16, 33, 79, 134, 135, 57, 43, 26, 11, 0, 0]
    with open("task4/results.txt", "r") as f:
        for line in f.readlines():
            l, r, dxe = map(int, line.split())
            cases.append((l, r))
            expected.append(dxe)
    for i in range(len(cases)):
        assert solution(
            *cases[i]) == expected[i], f"Expected {expected[i]} for {cases[i]}, but got {solution(*cases[i])}"
    print("All test cases passed")


def main():
    import time
    R = 10**14
    L = 1
    start = time.time()
    value = solution(L, R+1)
    end = time.time()
    print(f"Execution time: {round(end - start, 5)} seconds")
    pass


if __name__ == "__main__":
    test()
    main()
