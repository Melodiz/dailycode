from itertools import product
p1 = [3, 5, 7]
p2 = [11, 13, 17]
p3 = [19, 23, 29, 31, 37, 41, 43, 47]

result = []

for i in range(len(p2)):
    for j in range(len(p1)):
        result.append(p2[i] * p1[j])

print(len(set(result)))
