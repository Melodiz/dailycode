from functools import lru_cache


@lru_cache(maxsize=None)
def seq(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return seq(n//2)+1
    else:  # n % 2 == 1
        return seq(n+1) + seq(n//2)


def main():
    n = int(input())
    print(seq(n))


if __name__ == "__main__":
    main()
