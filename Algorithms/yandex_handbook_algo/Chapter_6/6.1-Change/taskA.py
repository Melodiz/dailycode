def print_change_by_trip(a, b, c):
    ans = str(a+b+c) + ' ' + '10 '*a + '5 '*b + '1 '*c
    print(ans.rstrip())

data = []
n = int(input())
for a in range(0, n//10+1):
    for b in range(0, (n-10*a)//5+1):
        for c in range(0, (n-10*a-5*b)+1):
            if a*10 + b*5 + c == n: data.append((a, b, c))

print(len(data))
for el in sorted(data, reverse=True):
    print_change_by_trip(*el)
