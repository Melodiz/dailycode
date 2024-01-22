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


for x in range(5,1000):
    for y in range(4,1000):
        f_n = 1*x**2+1
        s_n = 1*y**2+2
        if 2*f_n-s_n==1:
            print(x,y)
