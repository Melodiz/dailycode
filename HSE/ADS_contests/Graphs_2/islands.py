from collections import deque
import heapq

def solve(N, M, graph, baron_control):
    distances = [float('inf')] * N
    distances[0] = 0
    
    # Store only (cost, node) in priority queue
    priority_queue = [(0, 0)]
    # Track predecessors to reconstruct path later
    predecessor = [-1] * N
    
    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        
        if node == N-1: 
            # Reconstruct path only when needed
            path = []
            current = node
            while current != -1:
                path.append(current)
                current = predecessor[current]
            path.reverse()
            return cost, [p+1 for p in path]
        
        if cost > distances[node]:
            continue
        
        for neighbor in graph[node]:
            # Calculate toll cost (1 if crossing between different barons, 0 otherwise)
            toll = 1 if baron_control[node] != baron_control[neighbor] else 0
            new_cost = cost + toll
            
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                predecessor[neighbor] = node
                heapq.heappush(priority_queue, (new_cost, neighbor))
    
    return "impossible"

def main():
    N, M = map(int, input().split())
    baron_control = list(map(int, input().split()))
   
    baron_control = [b-1 for b in baron_control]
    
    # Build adjacency list
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1  
        b -= 1
        graph[a].append(b)
        graph[b].append(a)  
    result = solve(N, M, graph, baron_control)
    if result == "impossible":
        print("impossible")
    else:
        cost, path = result
        print(cost, len(path))
        print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()