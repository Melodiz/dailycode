import math
def gcd_array(B):
    gcd = B[0]
    for num in B[1:]:
        gcd = math.gcd(gcd, num)
    if gcd == 1:
        return True 
    return False

def beauty_seq(B):
    ans = 1
    for num in B:
        ans *= num
    return ans % 998244353

def beauty(p, q):
    gcd = math.gcd(p, q)
    return (p * q) // (gcd ** 2)

def check(B, A):
    for i in range(len(B)-1):
        if not beauty(B[i], B[i+1]) == A[i]:
            return False
    return gcd_array(B)

def brute(A):
    ans = 0
    from itertools import product
    for B in product(range(1, 100), repeat=len(A)+1):
        if check(list(B), A):
            print(B)
            ans += beauty_seq(B)
    return ans % 998244353

# def find_prev(current, a):
#     if (a/current)%1==0: return [x for x in range(1, 100)]
#     bprev = []
#     for candidate in range(1, 100):
#         if beauty(candidate, current) == a: bprev.append(candidate)
#     return bprev

if __name__ == "__main__":
    # print(brute([4]))
    # print(brute([4, 1]))
    # print(brute([4, 1, 1]))
    # print(brute([4, 1, 1, 2]))
    print(brute([3, 2, 4]))