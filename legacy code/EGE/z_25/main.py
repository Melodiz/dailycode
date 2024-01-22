def dns (n):
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            return(d)
    else:
        return 7

def chk_prime(n):
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            return False
    return True


data = []

for i in range(2,10**4):
    if chk_prime(i):
        data.append(i)

def ads(n):
    counter = 0
    for d in data:
        if n%d==0:
            counter +=1
        if counter >4:
            return d
    return 0
        
15
counter = 0

for num in range(800001, 10**10):
    if( dns(num)+(num/dns(num)))%138==0:
        print(num, int(dns(num)+(num/dns(num))))
        counter +=1

    if counter == 5:
        break

16
# from fnmatch import *

# for num in range(7,10**7):
#     if fnmatch(str(num), "34?8*9"):
#         if ads(num)!=0:
#             print(num, ads(num))