def solve(A, B, C, n):
    z = [0] * n
    z[0] = A[0]
    if n == 1: return z[0]
    z[1] = min(z[0]+A[1], B[0])
    for k in range(2, n):
        z[k] = min(z[k-1]+A[k], z[k-2]+B[k-1], z[k-3]+C[k-2])
    return z[n-1]



def main():
    n = int(input())
    A, B, C = [], [], []
    for _ in range(n):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    print(solve(A, B, C, n))



if __name__ == "__main__":
    main()