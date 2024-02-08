n, m, kol_vo = map(int, input().split())
cords = [list(map(int, input().split())) for x in range(kol_vo)]

area = [[-1 for x in range(m)] for x in range(n)]

def k(data, x,y):
    all_nea = [(x+1, y), (x+1,y+1), (x+1, y-1), (x, y+1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]
    count = 0
    for nea in all_nea:
        if 0<=nea[0]<m and 0<=nea[1]<n:
            if data[nea[1]][nea[0]]=='*': count+=1
    return str(count)

for x,y in cords:
    area[x-1][y-1]='*'

for y in range(n):
    for x in range(m):
        if area[y][x]!='*': area[y][x]=k(area,x,y)

for line in area:
    print(' '.join(line))