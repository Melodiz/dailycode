from functools import lru_cache

@lru_cache(maxsize=None)
def simple_seq(n):
    if n <= 1:
        return 1
    if n%2 == 0:
        return simple_seq(n//2) + simple_seq(n//2-1)
    else:
        return  simple_seq(n//2) - simple_seq(n//2-1)
    

def main():
    n = int(input())
    print(simple_seq(n))

if __name__ == "__main__":
    main()