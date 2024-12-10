from functools import lru_cache

@lru_cache(maxsize=None)
def rec(n, ll):
    if n == 0: return 1
    elif n < 0: return 0
    if ll == 0:
        return rec(n-1, 0) + rec(n-1, 1)
    else:
        return rec(n-1, 0)
    

def main():
    n = int(input())
    print(rec(n, 0))


if __name__ == "__main__":
    main()