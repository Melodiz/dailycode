
arr = []

for el in range(143146, 143215+1):
    arr.append(el)


for num in arr:
    x=0
    mass_d=[]
    for d in range(1, int(num/2)+1):
        if num%d == 0:
            x+=1
            mass_d.append(d)
    if x == 5:
        print(mass_d[-2], mass_d[-1])
