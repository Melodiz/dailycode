
def split_list(items):
    l = len(items)
    if l == 1:
        return [[items[0]],[]]
    elif l ==0:
        return [[], []]
    elif l%2==0:
        return [items[:int(l/2)],items[int(l/2):]]
    else:
        return [items[:int((l+1)/2)],items[int((l+1)/2):]]


print("Example:")
print(list(split_list([1, 2, 3, 4, 5, 6])))

assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"],
]
assert list(split_list([1])) == [[1], []]
assert list(split_list([])) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
