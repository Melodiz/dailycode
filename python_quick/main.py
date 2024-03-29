def rec(b, r, o, n):
    if n == 0:
        return (b, r, o)
    return rec(2*o, b+o, 2*r, n-1)


print(rec(5, 0, 0, 60))
print(f'({2**60 - 2**32}, {2**60+2**30}, {2**60+2**30})')