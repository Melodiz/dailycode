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

def counter_sorted_by_keys(arr):
    # it's just collections.Counter which is sorted by keys
    # I've implement it, because I'm not sure if we allowed to use it
    letters = merge_sort(list(set(arr)))
    result = {}
    for key in letters:
        result[key] = 0
    for el in arr:
        result[el] += 1
    return result


def main():
    n = int(input())
    data = list(input())
    letters_values = counter_sorted_by_keys(data)
    find_odd_flag = False
    odd_letter = ''
    ans = []
    for key, value in letters_values.items():
        ans.append([key, (value//2)])
        if not find_odd_flag and value % 2 != 0:
            odd_letter = key
            find_odd_flag = True
    for k, v in ans:
        print(k*v, end='')
    print(odd_letter, end='')
    for k, v in ans[::-1]:
        print(k*v, end='')
    return 0


if __name__ == "__main__":
    main()
