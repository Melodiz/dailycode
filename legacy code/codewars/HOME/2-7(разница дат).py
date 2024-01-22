def changing_direction(elements: list[int]) -> int:
    counter = 0
    x = 0
    for i in range(len(elements)):
        try:
            if elements[i] < elements[i-1] and elements[i-2] >= elements[i-1]:
                counter += 1
            elif elements[i] > elements[i-1] and elements[i-1] <= elements[i-2]:
                print(elements[i])
                counter += 1
        except:
            pass

    return counter


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
