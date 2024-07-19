from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_mod_10(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_mod_10(n-1) + fibonacci_mod_10(n-2)) % 10
    
def fibonacci_sum_last_digit(n):
    return fibonacci_mod_10((n+2)%60)-1 % 10
    

# find the last digit of sum of fibonacci numbers from 0 to n
print(fibonacci_sum_last_digit(int(input())))