def solve():
    n = int(input())
    r = list(map(float, input().split()))

    r1 = r[0]
    R_prime = sum(r[1:])
    norm_rprime_sq = sum(x*x for x in r[1:])
    
    if abs(norm_rprime_sq) < 1e-15:
        if abs(r1 - 1.0) < 1e-12:
            answer = float(n)
        else:
            answer = n*r1
    else:
        L = 1.0 + (1.0 - r1) * R_prime / norm_rprime_sq
        R_tot = r1 + R_prime
        answer = L * R_tot

    print(f"{answer:.3f}")

def main():
    solve()

if __name__ == "__main__":
    main()