from functools import lru_cache 


@lru_cache(maxsize=None)
def rec(n):
    if n == 0: return 1
    elif n < 0: return 0
    return rec(n-1) + rec(n-2) + rec(n-3)


def main():
    n = int(input())
    print(rec(n))

if __name__ == "__main__":
    main()