# 1886
def chek_primaries(n):
    for d in range(2, int(n**0.5)+2):
        if n % d == 0:
            return False
    return True


def all_divisions(n):
    data = set()
    for d in range(2, int(n**0.5)+2):
        if n % d == 0:
            data.add(d)
            data.add(int(n/d))
    return data


value = 0

a = 13*17*23*29*7
for num in range(970*a, 2*10**9, a):
    if num%3 != 0 and num%5 !=0:
        data = all_divisions(num)
        cout = 0
        for el in data:
            if el%2 == 1:
                cout+=1
        if cout > 100:
            value +=1

print(value)