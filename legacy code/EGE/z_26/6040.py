a = open('C:\main\code\EGE\z_26/a_26-100.txt').read()

a=a.split()

for l in range(len(a)):
    a[l]=int(a[l])
    
N=a[0];M=a[1];a=a[2:]

a=sorted(a, reverse=True)

print(a[119])


