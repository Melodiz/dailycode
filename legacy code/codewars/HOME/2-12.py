def missing_number(items: list[int]) -> int:
    arr = sorted(items)
    dist_1 = arr[-1]-arr[-2]
    dist_2 = arr[-2]-arr[-3]
    true_dist = 0
    if dist_1>=dist_2:
        true_dist = dist_2
    else:
        true_dist = dist_1

    for i in range(len(arr)+1):
        try:
            if arr[i]-arr[i-1]>true_dist:
                return arr[i]-true_dist
        except:
            pass

print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
