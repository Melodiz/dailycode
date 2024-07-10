def checkio(array: list[int]) -> int:
    if len(array) == 0:
        return 0
    x = 0

    for el in range(0, len(array), 2):

        x += array[el]

    return x*array[-1]


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")


