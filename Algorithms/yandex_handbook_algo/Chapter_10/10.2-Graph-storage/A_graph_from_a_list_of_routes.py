n, m = map(int, input().split())
data = [list(map(int, input().split()))[1:] for _ in range(m)]
vertex_list = [x for x in range(1, n+1)]

graph_1 = [[0 for _ in range(n)] for t in range(n)]

for route in data:
    for i in range(len(route)-1):
        graph_1[route[i]-1][route[i+1]-1] = 1
    for i in range(len(route), 1, -1):
        graph_1[route[i-1]-1][route[i-2]-1] = 1

for row in graph_1:
    print(*row)

graph_2 = [[0 for _ in range(n)] for _ in range(n)]

for route in data:
    route_set = set(route)
    for el in route_set:
        for goal in route_set:
            if el != goal:
                graph_2[el-1][goal-1] = 1


for row in graph_2:
    print(*row)