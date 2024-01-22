from functools import lru_cache
# from sys import setrecursionlimit
# from math import factorial

@lru_cache(None)
# setrecursionlimit(30000)

def F(n):
    if n<=3:
        return n
    elif n%2==1:
        return 2*n+F(n-2)
    else:
        return n**2+F(n-1)
        
for n in range(1, 10_000):
    F(n)

print(F(10000)-F(9995))

# print(F(999)-F(46))
