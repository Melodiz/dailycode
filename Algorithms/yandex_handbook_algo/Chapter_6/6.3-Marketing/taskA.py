n, k, w = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(k)]
balance = w*n
data.sort(reverse=True)

profit = 0
i = 0

while i < k and balance > 0:
    if data[i][1] <= balance:
        profit += data[i][0] * data[i][1]
        balance -= data[i][1]
        i += 1
    else:
        profit += data[i][0] * balance
        balance = 0
print(profit)