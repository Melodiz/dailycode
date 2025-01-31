def solve(n, k, nums):
    MOD = 998244353

    def f(p):
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                sum_pair = nums[i] + nums[j]
                result += pow(sum_pair, p, MOD)
        return result % MOD

    return [f(p) for p in range(1, k + 1)]

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    results = solve(n, k, nums)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()