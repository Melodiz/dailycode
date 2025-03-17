def find_negative_cycle(n, graph):
    dist = [0] * n
    pred = [-1] * n
    
    # Relax edges n times (instead of n-1 as in the Bellman-Ford algorithm)
    x = -1  # Will store a vertex that is part of a negative cycle
    for i in range(n):
        x = -1
        for u in range(n):
            for v in range(n):
                if graph[u][v] < 100000:  # If there is an edge
                    if dist[v] > dist[u] + graph[u][v]:
                        dist[v] = dist[u] + graph[u][v]
                        pred[v] = u
                        x = v
    
    # If no relaxation on the n-th iteration, no negative cycle
    if x == -1:
        return None
    
    for i in range(n):
        x = pred[x]
    
    # Reconstruct the cycle
    cycle = []
    v = x
    while True:
        cycle.append(v + 1)  # +1 because vertices are 1-indexed in output
        v = pred[v]
        if v == x and len(cycle) > 1:
            break
    
    cycle.append(cycle[0])  
    cycle.reverse()  
    return cycle

def main():
    n = int(input())
    graph = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    cycle = find_negative_cycle(n, graph)
    
    if cycle is None:
        print("NO")
    else:
        print("YES")
        print(len(cycle))
        print(" ".join(map(str, cycle)))

if __name__ == "__main__":
    main()