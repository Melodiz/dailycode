from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input())
k = 1
while(fibonacci(k) <= n):
    k += 1
print(fibonacci(k-2), fibonacci(k-1))