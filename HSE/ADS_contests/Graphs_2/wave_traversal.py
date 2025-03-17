from collections import deque, defaultdict

def wave_traversal(graph, start_vertex, n):
    # Calculate distances from start_vertex to all other vertices using BFS
    distances = [-1] * (n + 1)
    distances[start_vertex] = 0
    
    queue = deque([start_vertex])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    # Group vertices by their distance from start_vertex
    vertices_by_distance = defaultdict(list)
    for vertex in range(1, n + 1):
        if distances[vertex] != -1:  
            vertices_by_distance[distances[vertex]].append(vertex)
    

    traversal = []
    max_distance = max(vertices_by_distance.keys())
    
    for distance in range(max_distance + 1):
        if distance in vertices_by_distance:
            traversal.extend(vertices_by_distance[distance])
    
    return traversal

def main():
    n, m, v = map(int, input().split())
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v_i = map(int, input().split())
        graph[u].append(v_i)
        graph[v_i].append(u)  
    
    # Find wave traversal
    traversal = wave_traversal(graph, v, n)
    
    print(len(traversal))
    print(' '.join(map(str, traversal)))

if __name__ == "__main__":
    main()