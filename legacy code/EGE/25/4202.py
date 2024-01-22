ran = [3_000_000, 10_000_000]
start = ran[0]
end= ran[1]


def primeri_numbers(start, end):
    arr = [True]*end

    for i in range(2, len(arr)):
        if arr[i] == True:
            for el in range(i**2, len(arr), i):
                arr[el] = False
    output = []
    
    for el in range(2,len(arr)):
        if el >= start and arr[el] == True:
            output.append(el)

    return (output)

arr = primeri_numbers(start, end)

use_full_mass=[]

for i in range(len(arr)):
    if abs(arr[i]-arr[i-1])==2:
        use_full_mass.append(arr[i])
        use_full_mass.append(arr[i-1])

use_full_mass = set(use_full_mass)
use_full_mass = list(use_full_mass)
use_full_mass = sorted(use_full_mass)

print(f'кол-во пар = {int(len(use_full_mass)/2)}')

x=(use_full_mass[-1]+use_full_mass[-2])/2

print(f'среднее арефметическое ласт пары:{x}')