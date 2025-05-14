def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_all_divisors(n):
    data = []
    for b0 in range(1, int(n**0.5) + 1):
        if n % b0 == 0:
            b1 = n // b0
            if gcd(b1, b0) == 1:
                data.append((b0, b1))
            if b0 != n//b0:
                new_b0 = n//b0
                new_b1 = n // new_b0
                if gcd(new_b1, new_b0) == 1:
                    data.append((new_b0, new_b1))
    return data

def solve(A):
    data = dict()
    for b0, b1 in get_all_divisors(A[0]):
        data[b1] = A[0]
    # fill the rest
    for i in range(1, len(A)):
        iteration_data = dict()
        b0b1 = get_all_divisors(A[i])
        for b0, b1 in b0b1:
            for b_i, s_i in data.items():
                b_new = (b1*b_i) // gcd(b_i, b0)
                sum_new = s_i * b_new * ((b0 // gcd(b_i, b0)) ** (i+1))
                iteration_data[b_new] = (iteration_data.get(
                    b_new, 0) + sum_new) % 998244353
        data = iteration_data
    return sum(data.values()) % 998244353


if __name__ == "__main__":
    _ = input()
    arr = list(map(int, input().split()))
    print(solve(arr))
