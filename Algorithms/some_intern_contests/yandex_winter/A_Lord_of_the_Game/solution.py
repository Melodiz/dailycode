def find_min_max(values):
    min_val, max_val = float('inf'), float('-inf')
    for i in range(len(values)):
        if values[i] < min_val:
            min_val = values[i]
        if values[i] > max_val:
            max_val = values[i]
    return min_val, max_val


def solve(values, n):
    min_val, max_val = find_min_max(values)
    # first variant : left_index < right_index
    left_index, right_index = -1, -1
    result = 0
    for i in range(n):
        if values[i] == min_val:
            left_index = i
            break
    for i in range(n - 1, -1, -1):
        if values[i] == max_val:
            right_index = i
            break
    result = sum(values[min(left_index, right_index):max(right_index, left_index) + 1])
    # second variant : left_index > right_index
    left_index, right_index = -1, -1
    for i in range(n-1, -1, -1):
        if values[i] == min_val:
            left_index = i
            break
    for i in range(n):
        if values[i] == max_val:
            right_index = i
            break
    result = max(sum(values[min(left_index, right_index):max(right_index, left_index) + 1]), result)
    return result   


def main():
    n = int(input())
    values = list(map(int, input().split()))
    print(solve(values, n))


if __name__ == "__main__":
    main()