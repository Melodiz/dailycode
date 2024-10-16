def merge(arr1, arr2):
    l, r = 0, 0
    result = []
    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            result.append(arr1[l])
            l += 1
        else:
            result.append(arr2[r])
            r += 1
    if l >= len(arr1):
        return result + arr2[r:]
    return result + arr1[l:]


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        left_half = merge_sort(arr[:n//2])
        right_half = merge_sort(arr[n//2:])
        return merge(left_half, right_half)


def main():
    n = input()
    arr = list(map(int, input().split()))
    print(*merge_sort(arr))
    return 0


if __name__ == '__main__':
    main()
