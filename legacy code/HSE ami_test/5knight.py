from sys import exit
i = list(map(int, input().split()))
M, N, p, q, X1, Y1, X2, Y2 = i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]
start = (X1,Y1)
end = (X2,Y2)
fx,fy = min(p,q), max(p,q)

full_data_end_to_start = [[(X2,Y2)]]

moves_for_game = 0
flag = False

for move_number in range(1,100):
    this_itter_moves = set()
    for place in full_data_end_to_start[-1]:
        x,y = place[0],place[1]
        varrs = [(x+fx, y+fy),(x+fx, y-fy),(x-fx, y-fy),(x-fx, y+fy),
        (x+fy, y+fx),(x+fy, y-fx),(x-fy, y+fx),(x-fy, y-fx)]
        for var in varrs:
            if 1<=var[0]<=M and 1<=var[1]<=N:
                this_itter_moves.add(var)
    full_data_end_to_start.append(list(this_itter_moves))
    if start in this_itter_moves:
        flag=True; moves_for_game = move_number
        break

# table_end_to_start = [[-1 for x in range(M)] for x in range(N)]

# for deep in range(len(full_data_end_to_start)):
#     for el in full_data_end_to_start[deep]:
#         x,y = el
#         if table_end_to_start[N-y][x-1] == -1:
#             table_end_to_start[N-y][x-1] = deep
#         else:
#             table_end_to_start[N-y][x-1] = min(deep, table_end_to_start[N-y][x-1])

# print(full_data_end_to_start)
# for line in table_end_to_start:
#     print(line)
# exit(0) 

if not flag:
    print(-1)
    exit(0)

# now we find all places from end to start
# let's find road from start to end

right_way = [start]

for move_number in range(1,moves_for_game+1):
    place = right_way[-1]
    x,y = place[0],place[1]
    varrs = [(x+fx, y+fy),(x+fx, y-fy),(x-fx, y-fy),(x-fx, y+fy),
    (x+fy, y+fx),(x+fy, y-fx),(x-fy, y+fx),(x-fy, y-fx)]
    for var in varrs:
        if var in full_data_end_to_start[len(full_data_end_to_start)-move_number]:
            right_way.append(var)
            break

right_way.append(end)
print(moves_for_game)
for move in right_way:
    print(move[0],move[1])


# 8 8 1 2 3 1 8 5