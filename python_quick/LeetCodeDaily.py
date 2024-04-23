for x in range(-150, 150):
    for y in range(-150, 150):
        x = x/100
        y = y/100
        if (x**3 + y**3)**1/3 > x**2 + y**2:
            print(x,y)

print('end')