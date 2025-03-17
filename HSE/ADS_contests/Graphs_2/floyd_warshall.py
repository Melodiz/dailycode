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
        row = list(map(int, input().split()))
        graph.append(row)
    
    shortest_paths = floyd_warshall(graph)
    
    for row in shortest_paths:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()