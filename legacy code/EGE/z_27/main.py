a = open("C:\main\code\EGE\z_27\z_27-B.txt").readlines()
a = a[1:]

data_0 = []
data_1 = []
data_2 = []

for el in a:
    if int(el)%3 == 0:
        data_0.append(int(el)%4096)
    elif int(el)%3 == 1:
        data_1.append(int(el)%4096)
    elif int(el)%3 == 2:
        data_2.append(int(el)%4096)

from collections import Counter

c_data_0 = Counter(data_0)
c_data_1 = Counter(data_1)
c_data_2 = Counter(data_2)

counter = 0

for el in (c_data_0):
    for le in (c_data_0):
        if (el*le)%4096 == 0:
            if el == le:
                counter += c_data_0[el]*(c_data_0[le]-1)
            else:
                counter += c_data_0[el]*c_data_0[le]

counter = counter/2

for el in (c_data_1):
    for le in (c_data_2):
        if (el*le)%4096 == 0:
            counter += c_data_1[el]*c_data_2[le]
        

print(counter)

# 572 809 515
# 572 809 515
