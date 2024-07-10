from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    """    a = ''
        for el in items:
            a += str(el)

        b = a.find(str(border))
        if b == -1:
            return items

        # print(items[b:])
        return items[b:]

        почему не работает?
    """

    try:
        inx = items.index(border)

    except:
        return items

    return(items[inx:])




print("Example:")
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_before([], 0)) == []
assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")


# Output - "Hire the top freelancers"
