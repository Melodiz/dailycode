N, t = list(map(int, input().split()))
data = [list(map(int, input().split())) for t in range(N)]

for iter in range(t):
    after = [[0 for el in range(N)] for x in range(N)]
    for line in range(N):
        for ci in range(N):
            k = 0
            vars = ((line, ci-1), (line, ci+1), (line-1, ci), (line+1, ci), (line+1, ci+1),
                     (line+1, ci-1), (line-1, ci-1), (line-1, ci+1))
            for var in vars:
                if 0<=var[0]<N and 0<=var[0]<N and 0<=var[1]<N and 0<=var[1]<N and data[var[0]][var[1]]==1:
                    k+=1
            if k>3: after[line][ci]=0
            elif k<2: after[line][ci]=0
            elif k==2: after[line][ci]=data[line][ci]
            else: after[line][ci]=1
    data = after


print('______')
for line in data:
    s = ''
    for el in line: s+=str(el)+' '
    print(s)
    
