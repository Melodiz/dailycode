n = int(input())
data = [input().split() for x in range(2*n)]

ans = set(data[1])

for i in range(3,2*n,2):
    ans = ans.intersection(set(data[i]))

print(len(ans))
print(" ".join(sorted(list(ans))))


        