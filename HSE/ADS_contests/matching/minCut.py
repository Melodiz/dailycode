from collections import deque

def bfs(graph, source, sink, parent):
    n = len(graph)
    visited = [False] * n
    queue = deque()
    
    queue.append(source)
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    
    return visited[sink]

def ford_fulkerson(graph, source, sink):
    n = len(graph)
    capacity = [row[:] for row in graph]
    
    parent = [-1] * n
    max_flow = 0
    
    while bfs(capacity, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow  
            v = parent[v]
    
    return max_flow, capacity

def find_min_cut(graph, source, sink):
    n = len(graph)
    max_flow, residual_graph = ford_fulkerson(graph, source, sink)
    
    visited = [False] * n
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and residual_graph[u][v] > 0:
                visited[v] = True
                queue.append(v)
    
    min_cut_edges = []
    min_cut_capacity = 0
    
    for i in range(1, n):
        for j in range(1, n):
            if visited[i] and not visited[j] and graph[i][j] > 0:
                min_cut_edges.append((i, j))
                min_cut_capacity += graph[i][j]
    
    return min_cut_edges, min_cut_capacity

def main():
    n, m = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    edges = []
    
    for i in range(m):
        u, v, capacity = map(int, input().split())
        graph[u][v] = capacity
        graph[v][u] = capacity  
        edges.append((u, v))
    
    min_cut_edges, min_cut_capacity = find_min_cut(graph, 1, n)
    
    min_cut_indices = []
    for edge in min_cut_edges:
        u, v = edge
        for i, (a, b) in enumerate(edges, 1):
            if (u == a and v == b) or (u == b and v == a):
                min_cut_indices.append(i)
                break
    
    min_cut_indices = sorted(set(min_cut_indices))
    
    print(len(min_cut_indices), min_cut_capacity)
    print(" ".join(map(str, min_cut_indices)))

if __name__ == "__main__":
    main()