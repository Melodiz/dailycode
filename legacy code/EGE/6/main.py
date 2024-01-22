from turtle import *
m = 100
tracer(0)

begin_fill()
left(90)

for i in range(3):
    for j in range(3):
        fd(6*m)
        rt(120)
    rt(120)

update()
end_fill()

canvas = getcanvas()
cnt = 0
for x in range(-120*m, 120*m, m):
    for y in range(-120*m, 120*m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            cnt += 1
        # if len(item) >= 1:
        #     cnt += 1

print(cnt)
done()
# exit()
                    