from typing import Iterable


def split_pairs(line):
    n = 2
    new_list = []
    for i in range(0, len(line), n):
        element = line[i:i+n]
        if len(element) == 1:
            new_list.append(element + '_')
        else:
            new_list.append(element)
    
    return new_list

print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
