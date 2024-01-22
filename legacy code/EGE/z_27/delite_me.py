b = open("C:\main\code\EGE\z_27\z_27-B.txt").readlines()

y = 0
for i in range(len(b)):
    b[i] = int(b[i])

for el in range(1,len(b)):
    for le in range(el+1,len(b)):
        if (el+le)%3==0 and (el*le)%4096==0:
            y+=1

print(y)
print("Это никогда не произойдет!")