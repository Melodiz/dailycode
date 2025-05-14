def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_all_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return divisors

def find_b0_b1(A):
    data = []
    div0 = get_all_divisors(A)
    for b0 in div0:
        b1 = A // b0
        if gcd(b1, b0) == 1:
            data.append((b0, b1))
    return data

def solve(A):
    data = dict()
    for b0, b1 in find_b0_b1(A[0]):
        data[b1] = A[0]
    # fill the rest
    for i in range(1, len(A)):
        iteration_data = dict()
        b0b1 = find_b0_b1(A[i])
        for b0, b1 in b0b1:
            for b_i, s_i in data.items():
                b_new = (b1*b_i) // gcd(b_i, b0)
                sum_new = (s_i *  b_new * ((b0 // gcd(b_i, b0)) ** (i+1))) % 998244353
                iteration_data[b_new] = (iteration_data.get(b_new, 0) + sum_new) % 998244353
        data = iteration_data
    return sum(data.values()) % 998244353

if __name__ == "__main__":
    print(solve([4, 1, 1, 2]))  # 712 
    print(solve([4]))  # 8
    print(solve([3, 2, 4]))  # 9120
    print(solve([8, 5, 3, 2, 6, 4, 3, 6, 1, 2, 5]))  # 581635566
    print(solve([6, 10, 15]))  # 30420000
    print(solve([2, 3, 2]))  # 720
