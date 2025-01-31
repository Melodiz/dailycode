def find_min_max_values(A, start, end):
    min_val = A[start]
    max_val = A[start]

    for i in range(start + 1, end + 1):
        if A[i] < min_val:
            min_val = A[i]
        if A[i] > max_val:
            max_val = A[i]

    return min_val, max_val

def price_for_this_window(A, start, end, l, h):
    min_val, max_val = find_min_max_values(A, start, end)
    p1 = max(0, l-min_val)
    p2 = max(0, max_val - h)
    return p1 + p2


def min_operations_to_adjust_range(A, m, l, h):
    A.sort()

    ans = float('inf')
    
    for i in range(len(A) - m + 1):
        L = A[i]
        R = A[i + m - 1]
        cover_cost = price_for_this_window(A, i, i + m - 1, l, h)
        
        if cover_cost < ans:
            ans = cover_cost
    return ans

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    l, h = A[0], A[1]
    
    result = min_operations_to_adjust_range(A[2:], m, l, h)
    print(result)

if __name__ == "__main__":
    main()
    # n, m = 14, 11
    # A = list(map(int, '41 39 98 61 4 60 21 95 99 17 32 55 35 33'.split()))
    # l, h = 17,60
    # print(min_operations_to_adjust_range(A, m, l, h)) # 14