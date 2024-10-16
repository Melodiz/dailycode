def get_max(arr):
    return max(arr)

def count_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    m = get_max(arr)

    # Do counting sort for every digit.
    # exp is 10^i where i is current digit number
    exp = 1
    while m // exp > 0:
        count_sort(arr, exp)
        exp *= 10

    total_sum = sum(arr[i] * (i + 1) for i in range(len(arr)))
    print(total_sum)

cur = 0  # unsigned 32-bit number
a = 0
b = 0

def next_rand24():
    global cur
    cur = (cur * a + b) & 0xFFFFFFFF  # Simulate overflow
    return cur >> 8  # number from 0 to 2^24 - 1

def next_rand32():
    x = next_rand24()
    y = next_rand24()
    return (x << 8) ^ y  # number from 0 to 2^32 - 1

def main():
    global a, b
    t, n = map(int, input().split())
    a, b = map(int, input().split())

    for _ in range(t):
        arr = [next_rand32() for _ in range(n)]
        radix_sort(arr)

if __name__ == "__main__":
    main()