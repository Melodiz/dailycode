def is_possible(data, capacity):
    # Sort the data by time, and in case of tie, by type (start before end)
    data.sort(key=lambda x: (x[0], not x[1]))

    current_overlaps = 0

    for point in data:
        if point[1]:  # start of a line
            current_overlaps += 1
            if current_overlaps > capacity:
                return False
        else:  # end of a line
            current_overlaps -= 1

    return True

def add_end_points(data, value):
    new_data = data[:]
    for point in data:
        if point[1]:
            new_data.append((point[0] + value, False))
    return new_data

def binary_search(data, capacity):
    left, right = 0, 2**31
    upper = right

    while left < right:
        mid = (left + right) // 2
        new_data = add_end_points(data, mid)
        if is_possible(new_data, capacity):
            left = mid + 1
        else:
            right = mid

    if left == 0:
        return "Impossible"
    if left == upper:
        return "INF"
    return str(left)

if __name__ == "__main__":
    n, capacity = map(int, input().split())
    data = [(int(input()), True) for _ in range(n)]
    print(binary_search(data, capacity))