mask = "3 2 * 5 4 ? 1 2 3 "

arr = []

start = 32_540_262

end = 10**13

dwa = ["1","2","3","4","5","6","7","8","9"]

for el in dwa:
    for firs in dwa:
        for two in dwa:
            for tri in dwa:
                for four in dwa:
                    l = '32'+firs+two+tri+four+'54'+el+'123'
                    if int(l)%519 ==0:
                        arr.append(int(l))
    for firs in dwa:
        for two in dwa:
            l = '32'+firs+two+'54'+el+'123'
            if int(l)%519 ==0:
                arr.append(int(l))
    l = '32'+firs+two+'54'+el+'123'
    if int(l)%519 ==0:
        arr.append(int(l))

for el in arr:
    x = 0
    el = str(el)
    b = 0
    m = int(len(el)/2)
    for j in el[:m]:
        x += int(j)
    for j in el[m:]:
        b += int(j)
    if x == b:
        el = int(el)
        print(f'{el} - {int(el/519)}')






