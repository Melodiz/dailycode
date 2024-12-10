def main():
    n = int(input())
    data = [int(i) for i in input().split()]
    data.sort()
    d = [0] * n
    d[1] = data[1] - data[0]
    if n > 2:
            d[2] = data[2] - data[0]
            for i in range(3, n):
                    d[i] = min(d[i - 2], d[i - 1]) + data[i] - data[i - 1]
    print(d[n - 1])


if __name__ == "__main__":
    main()
