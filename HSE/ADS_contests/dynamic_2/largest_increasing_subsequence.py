def binary_search(data, x):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == x:
            return mid
        elif data[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


def LIS(arr):
    data = []
    data.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] > data[-1]:
            data.append(arr[i])
        else:
            pos = binary_search(data, arr[i])
            data[pos] = arr[i]
    return len(data)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(LIS(arr))
    return 0

if __name__ == "__main__":
    main()
