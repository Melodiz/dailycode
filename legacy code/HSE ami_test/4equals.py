import math
inp = list(map(int, input().split()))
a, b, c = inp[0], inp[1], inp[2]

discr = b ** 2 - 4 * a * c

if a == 0 and b!=0:
    x = -c/b
    print(1)
    print("%.6f" % x)
elif a==0 and b==0 and c!=0:
    print(0)
elif a==0 and b==0 and c==0:
    print(-1)
elif discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    x1,x2 = min(x1,x2), max(x1,x2)
    print(2)
    print("%.6f \n%.6f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print(1)
    print("%.6f" % x)
else:
    print(0)