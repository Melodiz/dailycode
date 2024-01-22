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


start = 3
end = 1_000_000
b= []

arr = primeri_numbers(start, end)

for i in range(len(arr)):
    if i >= 1 and (abs(arr[i] - arr[i-1])-1)>=90:
        b.append(arr[i])
        b.append(arr[i-1])

print(sorted(b))







