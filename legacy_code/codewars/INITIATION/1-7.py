def end_zeros(a: int) -> int:
    l = ''.join(reversed(str(a)))
    x=0
    for el in l:
        if el != "0":
            return x
        else:
            x+=1
    return(x)





assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")

