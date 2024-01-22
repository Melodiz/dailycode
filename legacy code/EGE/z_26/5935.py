a = open("C:\main\code\EGE\z_26/26-98.txt").readlines()

kazna = int((a[0].split())[1])
data = []
for el in a[1:]:
    eli = el.split()
    eli[0]= int(eli[0])
    data.append(eli)

aviasales = []

for el in data:
    if el[1]=='BC':
        aviasales.append((el[0]*0.8))
    elif el[1]=='AC':
        aviasales.append((el[0]*0.9))
    else:
        aviasales.append(el[0])
    
ultra_mega_tovary = []

for i in range(len(data)):
    ultra_mega_tovary.append([aviasales[i],data[i][0]])

ultra_mega_tovary=sorted(ultra_mega_tovary)

data=[]

for tov in ultra_mega_tovary:
    if kazna-tov[0]>=0:
        data.append(tov)
        kazna-=tov[0]

print(round(150000-kazna))

kazna+=data[-1][0]

for el in sorted(ultra_mega_tovary, reverse=True):
    if el[0]!=el[1] and kazna-el[0]>=0:
        print(el[0])
        break

