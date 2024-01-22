st = 2
end = int(55555/2)


def primeri_numbers(start, end):
    arr = [True]*end

    for i in range(2, len(arr)):
        if arr[i] == True:
            for el in range(i**2, len(arr), i):
                arr[el] = False
    output = []

    for el in range(2, len(arr)):
        if el >= start and arr[el] == True:
            output.append(el)

    return (output)

mass = {}

arr = primeri_numbers(st, end)

for num in range(33333, 55555):
    x = 0
    
    for el in arr:

        if num % el == 0:
            x += el
    if x>250 and num%x==0:
        mass[num]=x

    
for el in mass:
    print(el, mass[el])