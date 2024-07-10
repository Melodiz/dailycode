n,k = map(int, input().split())
data = list(map(int, input().split()))

c = 0

for a in range(len(data)):
    for b in range(a, len(data)):
        if sum(data[a:b+1])==k: c+=1

print(c)