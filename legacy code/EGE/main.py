
# b = [1,3,8,17,3*8,17*8, 17*3,17*8*3]
# for x in b:
#     for y in b:
#         for p in range(-1000,10000):
#             if 7*x*p == 16*y*p - 73 and x!=y:
#                 print(x, y, p)
    
# print("XXX")


for x in range(100):
    if (7*x+73)%16 == 0:
        print(x)