from functools import lru_cache

@lru_cache(maxsize=None)
def rec(n, prev):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    if prev == 'A': return rec(n-1, 'B') + rec(n-1, 'C')
    else:
        return rec(n-1, 'A') + rec(n-1, 'B') + rec(n-1, 'C')
    

def main():
    n = int(input())
    print(rec(n-1, 'A') + rec(n-1, 'B') + rec(n-1, 'C'))

if __name__ == "__main__":
    main()