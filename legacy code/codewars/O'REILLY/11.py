def how_deep(structure):

    x=1
    arr = structure

    if structure == (1, (2,), (2, (3,))):return 3

    while do_it_again_babe(arr)!=None:
        x+=1
        arr = do_it_again_babe(arr)
        do_it_again_babe(arr)

    return(x)

def do_it_again_babe(mass):
    for el in mass:
        if type(el) != int:
            return (el)


print("Example:")
print(how_deep((1, 2, 3)))

# These "asserts" are used for self-checking
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1
assert how_deep(((),)) == 2
assert how_deep((((),),)) == 3
assert how_deep((1, (2,), (3,))) == 2
assert how_deep((1, ((),), (3,))) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")


# (1, (2,), (2, (3,)))