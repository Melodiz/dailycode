a = open("C:\main\code\EGE\z_26/26-97.txt").readlines()

kol_vo_trub = a[0]

data = []

for el in a[1:]:
    m = el.split()
    m[0], m[1] = int(m[0]), int(m[1])
    m.append(m[0]-2*m[1]-3)
    b=[m[2], m[0], m[1]]

    data.append(b)

data = sorted(data, reverse=True)

d = data[0][0]

arr = [data[0]]

for el in data:
   
    if d>=el[1]: 
        # print(d)
        d=el[0]
        arr.append(el)

print(len(arr), arr[-1])

arr = arr[:-1]

print(arr[-1])

for el in data:
    print(el[1]) 

# ->>106


