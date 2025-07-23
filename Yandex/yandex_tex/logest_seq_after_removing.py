# given a binary array, return max lenght of subarray of 1's 
# after removing one element from initial array
# you must remove 1 elemnt

# [1, 1, 0, 1, 1] # 5, left = 0, right = 5
def solve(a):
    left, right, seen = 0, 0, -1
    ans = 0
    while right < len(a):
        if a[right]:
            ans = max(ans, right-left)
        else:
            ans = max(ans, right-left-1)
            if seen != -1:
                left = seen + 1
            seen = right
        right += 1
    ans = max(ans, right-left-1)
    return max(ans, 0)


if __name__ == "__main__":
    assert (solve([1, 1, 0, 1, 1]) == 4)
    assert (solve([1, 1, 0, 0, 1, 1, 0, 1]) == 3)
    assert (solve([0, 0]) == 0)
    assert (solve([0]) == 0)
    assert (solve([1]) == 0)
    assert (solve([1, 1, 1, 1, 1, 1])==5)
    print('All tests are passed!')
