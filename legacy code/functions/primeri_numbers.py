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