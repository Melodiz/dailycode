arr = open("C:\main\code\EGE\z_27\z_26.txt").readlines()

limit = arr[0]

arr = arr[1:]
limit = int(limit.split()[1])

modls = []

for el in arr:
    el = el.split()
    x = []
    x.append(int(el[0]))
    x.append(el[1])
    modls.append(x)

modls = sorted(modls)


bought = []

modls = sorted(modls)

counter_b = 0

one_time_l = limit
j = 0

while one_time_l > modls[j][0]:
    bought.append(modls[j])
    
    one_time_l -= modls[j][0];j += 1


mass_of_b_not_bought = []

for el in modls:
    if el not in bought and el[1] == "B":
        mass_of_b_not_bought.append(el)

mass_bought_A = []

for el in bought:
    if el[1] == "A":
        mass_bought_A.append(el)


mass_bought_A.reverse()

already_bought_b = 0

for el in bought:
    if el[1]=="B":
        already_bought_b+=1


v = 0
for el in mass_bought_A:
    if (one_time_l + el[0] - mass_of_b_not_bought[v][0])>=0:
        
        one_time_l += el[0] - mass_of_b_not_bought[v][0]
        v+=1
        already_bought_b+=1
        

        
print(already_bought_b, one_time_l)


"""
b = []

modls = sorted(modls)

counter_b = 0

one_time_l = limit
j = 0

while one_time_l >modls[j][0]:
    b.append(modls[j])
    j+=1
    one_time_l -= modls[j][0]

one_time_modls = []

total_cost_of_a = 0

p=0
for el in b:
    if el[1]=='A':
        total_cost_of_a += el[0]
        p+=1

print(total_cost_of_a,p)

for el in modls:
    if el[1]=="B" and el not in b:
        one_time_modls.append(el)


j_1 = 0; 

mass_of_needed_b=[]

while total_cost_of_a >one_time_modls[j_1][0]:
    mass_of_needed_b.append(one_time_modls[j_1])
    j_1+=1; total_cost_of_a -= one_time_modls[j_1][0]
"""

