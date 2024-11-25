def compute_lcp(s, suffix_array):
    n = len(s)
    rank = [0] * n
    lcp = [0] * (n - 1)
    
    for i in range(n):
        rank[suffix_array[i] - 1] = i
    
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1] - 1
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    
    return lcp

def main():
    n = int(input())
    s = input().strip()
    suffix_array = list(map(int, input().split()))
    
    lcp = compute_lcp(s, suffix_array)
    print(*lcp)

if __name__ == "__main__":
    main()