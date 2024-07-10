n = int(input())
data = list(map(int, input().split()))
goal = int(input())
data.append(goal)
data.sort()
x = data.index(goal)

if x == n:
    print(data[-2])
elif x == 0:
    print(data[1])
else:
    a = data[x+1]
    b = data[x-1]
    if abs(goal-a) < abs(goal-b):
        print(a)
    else:
        print(b)
