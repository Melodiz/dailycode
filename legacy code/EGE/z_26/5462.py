a = open("C:\main\code\EGE\z_26/26-96.txt").readlines()
a = a[1:]   

data = []
dolgots = []

for el in a:
    line = el.split()
    shirota = line[0]
    dolgota = line[1]
    dolgots.append(dolgota)
    try:
        shirota = shirota[:-1]
        arr = [int(dolgota), int(shirota)]
    except:
        arr = [int(dolgota), 0]

    data.append(arr)

data = sorted(data, reverse=True)


from collections import Counter

print(Counter(dolgots))

arr = []

for el in data:
    if el[0]==-162:
        arr.append(el[1])

print(len(Counter(arr)))