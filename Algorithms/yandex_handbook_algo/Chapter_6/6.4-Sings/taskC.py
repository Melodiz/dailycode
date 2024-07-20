def min_total_length(n, k, data):
    if k >= n:
        return 0

    data.sort()
    gaps = [data[i+1] - data[i] for i in range(n-1)]
    gaps.sort()

    return sum(gaps[:n-k])

if __name__ == "__main__":
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    result = min_total_length(n, k, data)
    print(result)