def SelectionSort(A):
    left, n = 0, len(A)
    while left < n:
        max_value = A[left]
        max_value_index = left
        for i in range(left, n):
            if max_value < A[i]:
                max_value = A[i]
                max_value_index = i
        A[left], A[max_value_index] = A[max_value_index], A[left]
        left += 1
    return A

if __name__ == "__main__":
    print(*SelectionSort(list(map(int, input().split()))))
