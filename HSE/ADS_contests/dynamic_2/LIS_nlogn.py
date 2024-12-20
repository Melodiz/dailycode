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


def LIS(n, k, b, m, a0):
    data = []
    ak = a0
    data.append(a0)
    for i in range(n-1):
        ak = (k * ak + b) % m
        if ak > data[-1]:
            data.append(ak)
        else:
            pos = binary_search(data, ak)
            data[pos] = ak
    return len(data)


def main():
    n, a0, k, b, m = map(int, input().split())
    print(LIS(n, k, b, m, a0))
    return 0

if __name__ == "__main__":
    main()
