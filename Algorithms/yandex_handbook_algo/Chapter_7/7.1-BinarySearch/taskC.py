def BinarySearch_FindLeft(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def BinarySearch_FindRight(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def findRange(arr, target):
    left = BinarySearch_FindLeft(arr, target)
    right = BinarySearch_FindRight(arr, target)

    if left == -1 or right == -1:
        return 0
    else:
        return right - left + 1
    
n = int(input())
arr = list(map(int, input().split()))
q = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(findRange(arr, target), end=' ')