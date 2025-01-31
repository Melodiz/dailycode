def build_binomial(max_n):
    """
    Build a 2D table comb so that comb[n][r] = C(n, r) mod MOD
    for all n, r up to max_n.
    """
    comb = [[0]*(max_n+1) for _ in range(max_n+1)]
    for i in range(max_n+1):
        comb[i][0] = 1
        for j in range(1, i+1):
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % 998244353
    return comb

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    MOD = 998244353
    
    # Precompute power sums S[l] = sum of b[i]^l for l=0..2k
    # This is potentially O(m * 2k), which can be large but is usually still feasible.
    S = [0]*(2*k+1)
    for x in a:
        cur = 1
        for l in range(2*k+1):
            S[l] = (S[l] + cur) % MOD
            cur = (cur * x) % MOD

    # Precompute binomial coefficients up to 2k
    comb = build_binomial(2*k)
    
    inv2 = (MOD + 1)//2   # modular inverse of 2 mod 998244353
    
    # Compute answers for p = 1..k
    answers = [0]*(k+1)
    for p in range(1, k+1):
        # Use the formulas described:
        # If p = 2q (even):
        #     f(p) = sum_{r=0..q-1} [ C(p,r) * (S[r]*S[p-r] - S[p]) ]
        #            + C(p,q) * ((S[q]^2 - S[p])/2)
        # If p = 2q+1 (odd):
        #     f(p) = sum_{r=0..q} [ C(p,r) * (S[r]*S[p-r] - S[p]) ]
        
        res = 0
        if p % 2 == 0:
            # even p = 2q
            q = p // 2
            for r in range(q):
                tmp = ((S[r] * S[p-r]) % MOD - S[p]) % MOD
                tmp = (tmp * comb[p][r]) % MOD
                res = (res + tmp) % MOD
            # middle term r = q
            tmp = ((S[q]*S[q]) % MOD - S[p]) % MOD
            tmp = (tmp * inv2) % MOD       # divide by 2
            tmp = (tmp * comb[p][q]) % MOD
            res = (res + tmp) % MOD
        else:
            # odd p = 2q+1
            q = (p - 1)//2
            for r in range(q+1):
                tmp = ((S[r] * S[p-r]) % MOD - S[p]) % MOD
                tmp = (tmp * comb[p][r]) % MOD
                res = (res + tmp) % MOD
        
        answers[p] = res % MOD
    
    # Output the answers
    out = []
    for p in range(1, k+1):
        out.append(str(answers[p]))
    print("\n".join(out))


if __name__ == "__main__":
    solve()