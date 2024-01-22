a,b = 120115,120200

x_max = 0
x_cur = 0

for num in range(a,b+1):
    x_cur = 0
    for m in range(1, round(num/2)+1):
        if num%m==0:
            x_cur+=1

    if x_cur >= x_max:
        x_max=x_cur
        print(num, x_cur+1)
        



print('finish')


a=225
l=0
for e in range(1,256):
    if a%e == 0:
        l+=1

print(l)


a=225
l=0
for e in range(1,16):
    if a%e == 0:
        l+=1

if a**0.5 == round(a**0.5):
    l = l*2-1

print(l)