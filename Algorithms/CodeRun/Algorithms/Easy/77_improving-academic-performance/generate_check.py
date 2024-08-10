import math
import random


def brut_force(a, b, c):
    s = 2*a+3*b+4*c
    amount = a+b+c
    for d in range(0, 10**12):
        if s/amount >= 3.5:
            return d
        s += 5
        amount += 1
    return -1


def control(a, b, c, d):
    def check(a, b, c, d):
        return (a*2 + b*3 + c*4 + d*5)/(a+b+c+d) >= 3.5
    if (check(a, b, c, d-1) and d > 0) or not check(a, b, c, d):
        return d-1
    return d


def classic_solution(a, b, c):
    def check(a, b, c, d):
        return (a*2 + b*3 + c*4 + d*5)/(a+b+c+d) >= 3.5
    left, right = 0, a+b+c + 1000
    while left < right:
        mid = (left + right) // 2
        if check(a, b, c, mid):
            right = mid
        else:
            left = mid + 1
    return left


def main():
    for test in range(100_000):
        a, b, c = random.randint(
            1, 10**5), random.randint(1, 10**5), random.randint(1, 10**5)
        cs_result = classic_solution(a, b, c)
        bf_result = control(a, b, c, cs_result)
        try:
            assert bf_result == cs_result
        except AssertionError:
            print(f"Test case failed for a={a}, b={b}, c={c}")
            print(f"brut_force result: {bf_result}")
            print(f"classic_solution result: {cs_result}")
            return
    print("All test cases passed")


if __name__ == "__main__":
    main()
