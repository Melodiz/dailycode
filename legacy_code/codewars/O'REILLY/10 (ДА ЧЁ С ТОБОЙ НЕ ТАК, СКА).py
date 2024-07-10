from collections import Counter


def frequency_sorting(numbers):
    arr = Counter(sorted(numbers)).most_common()
    output=[]

    for el in arr:
        for t in range(el[1]):
            output.append(el[0])

    return output




print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
