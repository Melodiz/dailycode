import heapq
from collections import defaultdict, deque

def shortest_paths(n, edges, s):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # Check if there are negative edges
    has_negative_edges = any(w < 0 for _, _, w in edges)
    
    if not has_negative_edges:
        # Use Dijkstra's algorithm for graphs with only non-negative weights
        return dijkstra(n, graph, s)
    else:
        # Use Bellman-Ford with negative cycle detection
        return bellman_ford_with_cycle_detection(n, edges, s)

def dijkstra(n, graph, s):
    dist = ['*'] * (n + 1)
    dist[s] = 0
    
    # Priority queue
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if dist[u] != d:
            continue
        
        for v, w in graph[u]:
            if dist[v] == '*' or dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist[1:]

def bellman_ford_with_cycle_detection(n, edges, s):
    dist = ['*'] * (n + 1)
    dist[s] = 0
    
    # Relaxation
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != '*' and (dist[v] == '*' or dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
    
    # Find vertices that are part of or reachable from negative cycles
    negative_cycle_vertices = set()
    
    # Additional relaxation to detect negative cycles
    for _ in range(n):
        for u, v, w in edges:
            if dist[u] != '*' and (dist[v] == '*' or dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                negative_cycle_vertices.add(v)
    
    # Find all vertices reachable from negative cycles
    reachable_from_negative = set()
    
    # Create a graph for BFS
    reachability_graph = defaultdict(list)
    for u, v, _ in edges:
        reachability_graph[u].append(v)
    
    # BFS from each vertex in a negative cycle
    for start in negative_cycle_vertices:
        queue = deque([start])
        visited = set([start])
        
        while queue:
            u = queue.popleft()
            reachable_from_negative.add(u)
            
            for v in reachability_graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
    
    # Mark vertices reachable from negative cycles with '-'
    for i in range(1, n + 1):
        if i in reachable_from_negative:
            dist[i] = '-'
    
    return dist[1:]

def main():
    n, m, s = map(int, input().split())
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    result = shortest_paths(n, edges, s)
    
    for d in result:
        print(d)

if __name__ == "__main__":
    main()