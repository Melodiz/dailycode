import heapq

def solve():
    n = int(input())
    a, b = map(int, input().split())
    k = int(input())
    
    graph = [[] for _ in range(n + 1)]

    # Create adjacency list
    for _ in range(k):
        start_point, start_time, end_point, end_time = map(int, input().split())
        graph[start_point].append((end_point, start_time, end_time))
    
    earliest_arrival = [float('inf')] * (n + 1)
    earliest_arrival[a] = 0
    
    pq = [(0, a)]
    
    while pq:
        current_time, current_node = heapq.heappop(pq)
        
        if current_time > earliest_arrival[current_node]:
            continue
        
        for next_node, departure_time, arrival_time in graph[current_node]:
            if current_time <= departure_time:
                if arrival_time < earliest_arrival[next_node]:
                    earliest_arrival[next_node] = arrival_time
                    heapq.heappush(pq, (arrival_time, next_node))
    
    return earliest_arrival[b]

print(solve())