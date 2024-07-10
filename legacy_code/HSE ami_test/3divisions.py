a =2**12-1
b = 2**9-1
def divs(n):
    data = set()
    for d in range(1, int(n**0.5)+1):
        if n%d==0: 
            data.add(n//d)
            data.add(d)
    return list(data)

da = sorted(divs(a))
db = sorted(divs(b))
print(da)
print(db)
ans = [x for x in da if x in db]

print(max(ans))
print(b)