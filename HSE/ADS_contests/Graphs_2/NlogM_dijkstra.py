import heapq

def dijkstra(edges, start, n):
    distances = [2009000999] * n
    distances[start] = 0
    

    pq = [(0, start)]
    visited = [False] * n
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if visited[current_vertex]:
            continue
        
        visited[current_vertex] = True
        
        for neighbor, weight in edges[current_vertex]:
            if visited[neighbor]:
                continue
                
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def main():
    num_tests = int(input())
    
    for _ in range(num_tests):
        n, m = map(int, input().split())
        
        edges = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v, w = map(int, input().split())
            
            edges[u].append((v, w))
            edges[v].append((u, w))
        
        for i in range(n):
            neighbor_weights = {}
            for neighbor, weight in edges[i]:
                if neighbor in neighbor_weights:
                    neighbor_weights[neighbor] = min(neighbor_weights[neighbor], weight)
                else:
                    neighbor_weights[neighbor] = weight
            
            edges[i] = [(neighbor, weight) for neighbor, weight in neighbor_weights.items()]
        
        start = int(input())
        
        # Run Dijkstra's algorithm
        distances = dijkstra(edges, start, n)
        
        # Print distances
        print(' '.join(map(str, distances)))

if __name__ == "__main__":
    main()