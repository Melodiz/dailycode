# 2592
def ckn(n):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True

data = []

for num in range(3, int((60*10**6)**(1/4))+1, 2):
    if ckn(num):
        data.append(num**4)

for num in data:
    for two in range(2, 20):
        if num*2**two in range(55_000_000, 60_000_000):
            print(num*2**two, num)
print('finish')
