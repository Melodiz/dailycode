def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    
    visited = [False] * n
    
    for _ in range(n):
        min_dist = float('inf')
        min_vertex = -1
        for v in range(n):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                min_vertex = v
        
        if min_vertex == -1:
            break
        
        visited[min_vertex] = True
        
        for v in range(n):
            if graph[min_vertex][v] != -1:
                if distances[min_vertex] + graph[min_vertex][v] < distances[v]:
                    distances[v] = distances[min_vertex] + graph[min_vertex][v]
    
    return distances[end] if distances[end] != float('inf') else -1

def main():
    n, s, f = map(int, input().split())
    
    # adjust to 0-based indexing
    s -= 1
    f -= 1
    
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    result = dijkstra(graph, s, f)
    
    print(result)

if __name__ == "__main__":
    main()