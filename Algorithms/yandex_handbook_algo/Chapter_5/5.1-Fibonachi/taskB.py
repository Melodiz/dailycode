from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_mod_10(n):
    return fibonacci(n%60) % 10
    
print(fibonacci_mod_10(int(input())))