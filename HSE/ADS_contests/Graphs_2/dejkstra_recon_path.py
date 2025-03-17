import heapq

def solve():
    line = input().split()
    N, S, F = map(int, line)
    
    # to 0-indexed 
    S -= 1
    F -= 1
    
    graph = []
    for _ in range(N):
        row = list(map(int, input().split()))
        graph.append(row)
    
    distances = [float('inf')] * N
    distances[S] = 0
    
    # Store (distance, vertex)
    priority_queue = [(0, S)]
    
    predecessor = [-1] * N
    
    while priority_queue:
        dist, vertex = heapq.heappop(priority_queue)
        
        if vertex == F:
            # Reconstruct path
            path = []
            current = vertex
            while current != -1:
                path.append(current + 1)  # Convert back to 1-indexed
                current = predecessor[current]
            path.reverse()
            return path
        
        if dist > distances[vertex]:
            continue
        
        for neighbor in range(N):
            if graph[vertex][neighbor] >= 0:  
                weight = graph[vertex][neighbor]
                if weight == -1: 
                    continue
                    
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessor[neighbor] = vertex
                    heapq.heappush(priority_queue, (new_dist, neighbor))
    
    return [-1]

def main():
    path = solve()
    print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()