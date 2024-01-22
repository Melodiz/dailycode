data = ([int(x) for x in open('17_2399.txt')])

ans = []

def conv(n,to):
    ans = []
    while n>0:
        ans.append(str(n%to))
        n=n//to
    return ''.join(ans[::-1])

avg = 0
for el in data:
    if el%35==0:
        for n in str(el):
            if n=='-':
                pass
            else:
                avg+=int(n)

print(avg)


for el in range(len(data)-1):
    a = data[el]
    b=data[el+1]
    if ((a>avg and b<=avg and hex(b)[-2:]=='ef') or (a<=avg and b>avg and hex(a)[-2:]=='ef')):
        ans.append(a+b)

print(len(ans), min(ans))
