from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items)!= 0:

        a=items[0]
        items.append(a)
        items.pop(0)
        return items

    return items

print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
