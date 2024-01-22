from fnmatch import *

k_r = 217
k=0

def dv(n):
    data = set()

    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            if d%2==1:
                data.add(d)
            if (n//d)%2==1:
                data.add(n//d)
    return data

data=[]


def sum_zf(n):
    x=0
    for el in str(n):
        x+=int(el)
    return x

for x in range(53847*13, 53847*14, 13):
    if not fnmatch(str(x), '*1*') and not fnmatch(str(x), '*0??3*') and not fnmatch(str(x), '*4??2'):
        print(x,sum_zf(x))
        k+=1
    if k==5:
        break
        


print('end')