def bellman_ford(n, edges, start=0):
    INF = 30000 # since then we can return 30000 if path doesn't exist
    distances = [INF] * n
    distances[start] = 0
    
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != INF and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    
    return distances

def main():
    n, m = map(int, input().split())
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        # Adjust to 0-indexed
        u -= 1
        v -= 1
        edges.append((u, v, w))
    
    distances = bellman_ford(n, edges, 0)

    print(' '.join(map(str, distances)))

if __name__ == "__main__":
    main()