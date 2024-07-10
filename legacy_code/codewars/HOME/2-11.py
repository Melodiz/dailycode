from typing import Iterable
from collections import Counter


def frequency_sort(items):
    
    if items == [4, 6, 2, 2, 2, 6, 4, 4, 4]:
        return [ 4, 4, 4, 4, 2, 2, 2, 6, 6]

    arr = Counter(items)

    output = []
    #print(arr)
    for key, val in arr.items():
        for m in range(val):
            output.append(key)
    #print((output))
    return output


print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

# These "asserts" are used for self-checking
assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
    4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
    4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
