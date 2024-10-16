def count_sort(n, arr):
    min_value, max_value = arr[0], arr[0]
    for el in arr:
        min_value = min(min_value, el)
        max_value = max(max_value, el)
    data = [0] * (max_value - min_value + 1)
    for el in arr:
        data[el - min_value] += 1
    sorted_arr = []
    for i in range(len(data)):
        sorted_arr.extend([i + min_value] * data[i])
    return sorted_arr

if __name__ == "__main__":
    print(*count_sort(int(input()), list(map(int, input().split()))))