def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
targets = list(map(int, input().split()))
for target in targets:
    print(binarySearch(arr, target))
