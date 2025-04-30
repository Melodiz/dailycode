from collections import deque

def MaxFlowMinCut(n, m, w, b, g, grid):
    s, t = 0, n * m + 1
    
    graph = [[] for _ in range(n * m + 2)]
    capacity = [[0] * (n * m + 2) for _ in range(n * m + 2)]
    
    def get_node(i, j):
        return i * m + j + 1
    
    # Precompute all nodes and edges
    for i in range(n):
        for j in range(m):
            node = get_node(i, j)
            
            if grid[i][j] == 'B':
                graph[s].append(node)
                graph[node].append(s)
                capacity[s][node] = w
            else:  # 'W'
                graph[node].append(t)
                graph[t].append(node)
                capacity[node][t] = b
            
            if j + 1 < m:
                neighbor = get_node(i, j + 1)
                graph[node].append(neighbor)
                graph[neighbor].append(node)
                capacity[node][neighbor] = g
                capacity[neighbor][node] = g
            
            if i + 1 < n:
                neighbor = get_node(i + 1, j)
                graph[node].append(neighbor)
                graph[neighbor].append(node)
                capacity[node][neighbor] = g
                capacity[neighbor][node] = g
    
    # Dinic's algorithm for faster max flow
    def bfs():
        level = [-1] * (n * m + 2)
        level[s] = 0
        q = deque([s])
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                if level[v] < 0 and capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        
        return level[t] >= 0
    
    def dfs(u, flow, level, ptr):
        if u == t:
            return flow
        
        while ptr[u] < len(graph[u]):
            v = graph[u][ptr[u]]
            
            if level[v] == level[u] + 1 and capacity[u][v] > 0:
                curr_flow = min(flow, capacity[u][v])
                temp_flow = dfs(v, curr_flow, level, ptr)
                
                if temp_flow > 0:
                    capacity[u][v] -= temp_flow
                    capacity[v][u] += temp_flow
                    return temp_flow
            
            ptr[u] += 1
        
        return 0
    
    max_flow = 0
    
    # Implement Dinic's algorithm
    while bfs():
        ptr = [0] * (n * m + 2)
        level = [-1] * (n * m + 2)
        level[s] = 0
        q = deque([s])
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                if level[v] < 0 and capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        
        while True:
            flow = dfs(s, float('inf'), level, ptr)
            if flow == 0:
                break
            max_flow += flow
    
    return max_flow

def main():
    n, m, w, b, g = map(int, input().split())
    grid = [input() for _ in range(n)]

    print(MaxFlowMinCut(n, m, w, b, g, grid))

if __name__ == "__main__":
    main()