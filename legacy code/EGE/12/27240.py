vals = list('1111111111222')
import itertools
perm_set = itertools.permutations(vals)

s_max = 0

for el in perm_set:
    start = ''.join(el)
    while '11' in start:
        if '112' in start:
            start = start.replace('112', '6')
        else: 
            start = start.replace('11', '3')
    s=0
    for el in start:
        s+=int(el)
    if s> s_max:
        s_max = s

print(s_max)

# 13! вариантов - долго, поэтому 112 112 112 1111 - максимум - 24