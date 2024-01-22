a = open("C:\main\code\EGE\z_27\m_26.txt").readlines()

data = []
kol_vo_process = a[0];a = a[1:]
START_TIME = 1633305600;END_TIME = 1633305600+3600*24*7
sec_mass = [0]*(3600*24*7)
x = 0;max_x=-1;t_max = 0


# оптимизированное решение:

for line in a:
    line = line.split()
    p = []
    p.append(int(line[0]))
    p.append(int(line[1]))
    data.append(p)


for procces in data:
    if procces[0] < START_TIME and (procces[1] > START_TIME or procces[1] == 0):
        x += 1
    if procces[0] >= START_TIME and (procces[0] <= END_TIME):
        sec_mass[procces[0]-START_TIME]+=1
    if procces[1]>=START_TIME and procces[1]<=END_TIME:
        sec_mass[procces[1]-START_TIME]-=1


for sec in sec_mass:
    x+=sec
    if max_x<x:
        max_x = x;t_max=0
    if max_x==x:
        t_max+=1

print(max_x, t_max)

# простое решение:
"""

for el in data:
    start_procc = el[0];end_procc=el[1]
    if el[0]==0:
        start_procc = START_TIME
    if el[1]==0:
        end_procc = END_TIME
    if (el[0]<=END_TIME or el[0]==0) and (el[1]>= START_TIME or el[1]==0):
        for sec in range(max(start_procc,START_TIME), min(end_procc, END_TIME)):
            sec_mass[sec]+=1

full_max=-1

for val in sec_mass.values():
    if val>full_max:
        full_max = val

x=0

for val in sec_mass.values():
    if val == full_max:
        x+=1

print(f'max_proc:{full_max}, time:{x}')

"""
