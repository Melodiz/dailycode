def sum_digits(num: int) -> int:

    while len(str(num)) > 1:
        x=0
        for dig in str(num):
            x+=int(dig)
        num = x
    return num

print("Example:")
print(sum_digits(38))

assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6
assert sum_digits(232) == 7
assert sum_digits(811) == 1
assert sum_digits(702) == 9

print("The mission is done! Click 'Check Solution' to earn rewards!")
