a, b = 123456789, 223456790

x_cur = 0
arr = []

kvadrs = []
max_del = 0
z = round(a**0.5)-1
while z**2 < b:
    kvadrs.append(z**2)
    z+=1
kvadrs.reverse()



for num in kvadrs:
    if num < a:
        break

    x_cur = 0

    for m in range(2, int(num**0.5)+1):
        if x_cur > 2:
            break
        elif num % m == 0:
            x_cur+=1
            if m != int(num**0.5):
                max_del = num/m
    if x_cur == 2:
        arr.append(int(max_del))
        arr.append(num)


print(arr)

print('finish')
