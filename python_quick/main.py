

for i in range(1, 129):
    count = 0
    k = i
    while (i != 1):
        if (i % 2 == 0):
            i = i / 2
        else:
            i = i + 1
        count += 1
    if (k == 2 or k== 4 or k == 8 or k == 16 or k == 32 or k == 64 or k == 128):
        print(f'{k} -> {count}')
    if (k == 6 or k == 12 or k == 24 or k == 48 or k == 96): 
        print(f'{k} -> {count}')
