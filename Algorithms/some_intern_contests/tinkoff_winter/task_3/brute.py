def check_valid(arr, low, hight, threshold):
    count = 0
    for num in arr:
        if low <= num <= hight:
            count += 1
    return count >= threshold


def bin_search(arr, init_low, init_hight, threshold):
    left = 0
    right = abs(init_low - min(arr)) + abs(init_hight - max(arr))
    
    while left < right:
        mid = (left + right) // 2
        if check_window_size(arr, init_low, init_hight, threshold, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def check_window_size(arr, init_low, init_hight, threshold, size):
    for i in range(0, size+1):
        low = init_low - (size - i)
        hight = init_hight + i
        if check_valid(arr, low, hight, threshold):
            return True
    return False


def solve_brute(A, m, l, h):
    n = len(A)
    threshold = m
    window_size = bin_search(A, l, h, threshold)
    return window_size

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    l, h = A[0], A[1]
    
    result = solve_brute(A[2:], m, l, h)
    print(result)

if __name__ == "__main__":
    main()
