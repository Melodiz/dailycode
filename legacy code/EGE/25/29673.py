a,b=200_000_000,400_000_000

k_two = []
k_tri =[]
arr = []


for i in range(0,10**4, 2):
    if 2**i>b:
        break
    k_two.append(2**i)

for i in range(1,10**4,2):
    if 3**i>b:
        break
    k_tri.append(3**i)

for two in k_two:
    for tri in k_tri:
        if two*tri <b and two*tri>a:
            arr.append(two*tri)
for i in sorted(arr):
    print(i)