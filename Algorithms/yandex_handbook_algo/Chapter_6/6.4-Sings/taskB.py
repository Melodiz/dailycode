def count_intervals(n, L, data):
    if not data:
        return 0

    data.sort()
    counter = 1
    current_end = data[0] + L

    for point in data:
        if point > current_end:
            counter += 1
            current_end = point + L

    return counter

if __name__ == "__main__":
    n, L = map(int, input().split())
    data = list(map(int, input().split()))

    result = count_intervals(n, L, data)
    print(result)