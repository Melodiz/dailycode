from collections import Counter

def checkio(data: list) -> list:
    count_d = Counter(data)
    duta = []
    for val in count_d:
        if count_d[val]!=1:
            duta.append(val)
    output = []
    for el in data:
        if el in duta:
            output.append(el)
    return(output)







print("Example:")
print(checkio([1, 2, 3, 1, 3]))

assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert checkio([1, 2, 3, 4, 5]) == []
assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
assert checkio([2, 2, 3, 2, 2]) == [2, 2, 2, 2]
assert checkio([10, 20, 30, 10]) == [10, 10]
assert checkio([7]) == []
assert checkio([0, 1, 2, 3, 4, 0, 1, 2, 4]) == [0, 1, 2, 4, 0, 1, 2, 4]
assert checkio([99, 98, 99]) == [99, 99]
assert checkio([0, 0, 0, 1, 1, 100]) == [0, 0, 0, 1, 1]
assert checkio([0, 0, 0, -1, -1, 100]) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
