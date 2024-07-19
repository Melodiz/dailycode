n, w = list(map(int, input().split()))
data = [int(input()) for _ in range(n)]
data.sort()


i = 0
while w > 0 and i < n:
    w -= data[i]
    i += 1

if w >= 0:
    print(i)
else:
    print(i-1)
