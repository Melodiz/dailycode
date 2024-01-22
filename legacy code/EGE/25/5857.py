def convert_base(num, from_base, to_base):

    if from_base == 10:
        arr = []
        while num >= to_base:
            arr.append(num % to_base)
            num = int(num/to_base)
        arr.append(num % to_base)
        arr.reverse()

        output = ''
        for el in arr:
            output += str(el)
        return output
    if to_base == 10:
        output = 0
        for el in str(num):
            output = output*from_base+int(el)
        return int(output)

arr = []

end = 10**9

dwa = ['0', "1", "2", "3", "4", "5", "6"]
kwa = ["1", "2", "3", "4", "5", "6"]

mask = "? 2 1 3 * 5 6 6 4"

for el in kwa:
    for firs in dwa:
        for two in dwa:
            x = el+'213'+ firs + two + '5664'

            x = convert_base(int(x), 7, 10)

            if x % 333 == 0 and x<10**9:
                arr.append(int(x))

    for firs in dwa:
        for two in dwa:
            for tri in dwa:
                x = el+'213'+firs +two+tri+ '5664'

                x = convert_base(int(x), 7, 10)

                if x % 333 == 0 and x<10**9:
                    arr.append(int(x))

    for firs in dwa:
        x = el+'213'+firs + '5664'

        x = convert_base(int(x), 7, 10)

        if x % 333 == 0:
            arr.append(int(x))
    x = el+'213'+'5664'

    x = convert_base(int(x),7, 10)

    if x % 333 == 0:
        arr.append(int(x))

for el in sorted(arr):

    print(f'{el} - {int(el/333)}')
print('finish')