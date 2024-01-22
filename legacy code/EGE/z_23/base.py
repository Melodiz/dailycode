# def Rec(n, end):
#     if n == end:
#         return 1
#     elif n > end:
#         return 0
#     return Rec(n+2, end) + Rec(n+4, end) + Rec(n+5, end)


# for x in range(1000):
#     if Rec(31, x) == 1001:
#         print(x)


# def bin_Rec(n,end):
#     if n==end:
#         return 1
#     elif len(n)>len(end):
#         return 0
#     a1 = str(bin(int(n,2)+1)[2:])
#     return bin_Rec(a1, end)+bin_Rec(n+'1', end)+bin_Rec(n+'0',end)

# print(bin_Rec('100','11101'))


# def kol_vo_Rec(n, end, c):
#     if n == end and c == 7:
#         return 1
#     elif n > end or c > 7:
#         return 0
#     return kol_vo_Rec(n+1, end, c+1) + kol_vo_Rec(n+4, end, c+1) + kol_vo_Rec(n*2, end, c+1)

# print(kol_vo_Rec(3,27,0))

from collections import Counter


def to_base_3(n):
    a = []
    while n > 0:
        a.append(str(n % 3))
        n = n//3
    return int(''.join(a[::-1]))


# d = set()


# def rec_hard(curr, step):
#     if step == 8:
#         d.add(curr)
#     else:
#         rec_hard(curr+1, step+1)
#         rec_hard(curr+5, step+1)
#         rec_hard(curr*3, step+1)


# x = 0

# rec_hard(1, 0)
# for el in list(d):
#     if el >= 1000 and el <= 1024:
#         x += 1


def rec(curr, end, k):
    if curr%2==0:
        k+=1
    if curr == end and k==6:
        return 1
    if curr>end or k>6:
        return 0
    return rec(curr+1, end, k) + rec(curr+3, end, k) + rec(curr+5, end, k)


print(rec(3,25, 0))