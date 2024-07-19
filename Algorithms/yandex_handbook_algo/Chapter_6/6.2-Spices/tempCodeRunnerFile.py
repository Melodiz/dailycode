n, w = list(map(int, input().split()))
data = [
    list(map(int, input().split()))
    for _ in range(w-1)
]
data.sort()

profit = 0
i = 0
while i < n:
    if data[i][1] <= w:
        profit += data[i][0] * data[i][1]
        w -= data[i][1]
        i += 1
    else:
        profit += data[i][0] * w
        break
print(profit)