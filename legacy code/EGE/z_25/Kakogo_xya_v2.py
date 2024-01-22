# 2594
def ckn(n):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True

print(ckn(557))

data = []

for num in range(int(int(113_000000/2)**0.5),int(int(114_000000/2)**0.5)+1):
    if ckn(num):
        data.append(num**2)

for num in data:
    if num*2 in range(113_000000, 114_000000):
        print(num*2, int(num**0.5)*2)

print("finish")