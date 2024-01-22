from functools import *
@lru_cache(None)

def check_prime(n):
    if n!= int(n):
        return 0
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            return 0
    return 1

def devisions(n):
    data = set()
    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            if d%2==1:
                data.add(d)
            if (n//d)%2==1:
                data.add(n//d)
    return data

deta = []

for el in range(113_000_000, 114_000_000,2):
    if check_prime((el//2)**0.5):
        print(el,int(2*(el//2)**0.5))
        



print('end') 