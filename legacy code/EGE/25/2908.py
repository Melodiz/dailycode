st = 586_132
end = 586_430

arr = []

for el in range(st, end+1):
    arr.append(el)

mass_d = {}


for num in arr:
    x = 1
    for d in range(1, (int(num/2)+1)):
        if num % d == 0:
            x += 1
    mass_d[num] = x

b = []

for keym, vl in mass_d.items():
    if vl == 80:
        b.append(keym)

print(sorted(b))


num_max = b[-1]
num_min = b[0]

a=0

for d in range(1, (int(num_max/2)+1)):
    if num_max % d == 0:
        a=d

print(f'{a} - макс делитель; для макс числа {num_max}')

for d in range(1, (int(num_min/2)+1)):
    if num_min % d == 0:
        a=d

print(f'{a} - макс делитель; для мин числа {num_min}')