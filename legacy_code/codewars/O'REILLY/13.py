def reverse_ascending(items):
"""    mass = []
    arr = []
    for i in range(1,len(items)):
        try:
            if items[i] < items[i+1]:
                arr.append(items[i])
            if items[i] >= items[i+1]:
                if len(arr)!=0:
                    mass.append(arr)
                arr = []
                mass.append(items[i])
        except:pass
    if len(arr)!=0:
        mass.append(arr)
    arr = []
    mass.append(items[-1])

    mass.reverse()
    return(mass)"""


def split_mass(arr):
    




print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
