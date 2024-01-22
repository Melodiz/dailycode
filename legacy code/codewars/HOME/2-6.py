def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    if a == b:
        return 0
    
    from datetime import datetime
    first = datetime(a[0],a[1],a[2])
    second = datetime(b[0],b[1],b[2])
    dif = abs(first-second)
    x = str(dif)
    for el in range(len(x)):
        if x[el] == ' ':
            print(x)
            return int(x[:el])


print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
assert days_diff((2014, 2, 28), (2014, 2, 28)) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
