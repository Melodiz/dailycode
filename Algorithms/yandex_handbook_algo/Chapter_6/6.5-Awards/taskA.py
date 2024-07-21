def check(k, n):
    return k*(k-1)/2 <= n

def binary_search(low, high, n):
    # find the highest value satisfying the condition check(k, n)
    while low <= high:
        mid = (low + high) // 2
        if check(mid, n):
            low = mid + 1
        else:
            high = mid - 1
    return high - 1

n = int(input())
print(binary_search(1, n, n))