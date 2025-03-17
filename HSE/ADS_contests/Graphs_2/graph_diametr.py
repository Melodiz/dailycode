def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def main():
    n = int(input())
    graph = []
    for _ in range(n):
        line = []
        for el in input().split():
            num = int(el) if el!= '-1' else float('inf')
            line.append(num)
        graph.append(line)
    shortest_paths = floyd_warshall(graph)
    
    diameter = 0
    radii = float('inf')
    for row in shortest_paths:
        diameter = max(diameter, max(row))
        radii = min(radii, max(row))
    print(diameter, radii)
    return diameter, radii

if __name__ == "__main__":
    main()