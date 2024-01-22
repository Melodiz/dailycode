start = 1_850_000_000

def gagachad(n):
    data = {}
    x=n
    for d in range(2, int(n**0.5)+1):
        if x%d==0 and ckn(d):
            data[d]=0
            while x%d == 0:
                x=x/d
                data[d]+=1
        if x%(x/d) == 0 and ckn(x/d):
            data[x/d]=0
            while x%(x/d )== 0:
                x=x/(x/d)
                data[x/d]+=1
    if data == {}:
        return False
    print(data)
    for val in data.values():
        if val%2!=0:
            return False
    ans = 1
    for el in data.values():
        ans = ans*(el+1)
    
    return ans

conter = 0

def ckn(n):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True


# for num in range(1_850_000_000+21_900, 1_850_000_000*2):
    
#     if gagachad(num):
#         print(num-1_850_000_000, gagachad(num))
#         conter +=1
#     if conter == 5:
#         break

print(gagachad(1_850_000_000+22792))

print('finish')