data = open("C:\main\code\EGE\z_26/26-99.txt").read()

data=data.split()

for i in range(len(data)):
    data[i]=int(data[i])

max_mass = data[1]; cars = data[0]; data = data[2:]
data = sorted(data, reverse=True)

car_info = {}

# print(len(data))


def car_input(data):
    mass = 1500
    whights = []

    for el in data:
        if mass-el>=0:
            whights.append(el)
            mass-=el
    # print(whights)
    for el in whights:
        data.remove(el)

    return(data, 1500-mass)


for car in range(cars+1):
    out_mass = car_input(data)
    data = out_mass[0]
    car_info[car]=out_mass[1]

for el, val in car_info.items():
    print(el, val)


"""УРАААА"""