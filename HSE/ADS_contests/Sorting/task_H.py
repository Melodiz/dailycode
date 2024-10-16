def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def reduce_fraction(numerator, denominator):
    g = gcd(numerator, denominator)
    return numerator // g, denominator // g


def bubble_sort_fractions(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][0] / arr[j][1] > arr[j+1][0] / arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    n, q = map(int, input().split())
    numerators = list(map(int, input().split()))
    denominators = list(map(int, input().split()))
    fractions = []
    for i in range(n):
        for j in range(n):
            reduced = reduce_fraction(numerators[i], denominators[j])
            fractions.append(reduced)
    sorted_fractions = bubble_sort_fractions(fractions)
    indexes = list(map(int, input().split()))
    for i in indexes:
        print(sorted_fractions[i-1][0], sorted_fractions[i-1][1])


if __name__ == "__main__":
    main()
