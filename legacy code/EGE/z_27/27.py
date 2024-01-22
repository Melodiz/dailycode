def Rec(n,end):
    if n==end:
        return 1
    elif n>end:
        return 0
    return (Rec(int(bin(n+1)[2:]),end) + Rec(n*10, end)+Rec(n*10+1, end))

# print(Rec(100,11101))

def bin_Rec(n,end):
    if n==end:
        return 1
    elif len(n)>len(end):
        return 0
    a1 = str(bin(int(n,2)+1)[2:])
    return bin_Rec(a1, end)+bin_Rec(n+'1', end)+bin_Rec(n+'0',end)
    
print(bin_Rec('100','11101'))