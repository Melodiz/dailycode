import sys
from collections import defaultdict

# Set the recursive limit to 10^7
sys.setrecursionlimit(10**7)

def find_cycle(graph, n):
    def dfs(node):
        visited[node] = True
        path[node] = True
        
        for neighbor in graph[node]:
            if path[neighbor]:
                # Found a cycle, reconstruct it
                cycle = [neighbor, node]
                current = node
                while current != neighbor:
                    current = parent[current]
                    cycle.append(current)
                return cycle[::-1]  # Reverse to get correct order
            
            if not visited[neighbor]:
                parent[neighbor] = node
                result = dfs(neighbor)
                if result:
                    return result
        
        path[node] = False
        return None

    visited = [False] * (n + 1)
    path = [False] * (n + 1)
    parent = {}

    for node in range(1, n + 1):
        if not visited[node] and node in graph:
            cycle = dfs(node)
            if cycle:
                return cycle

    return None  # No cycle found

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u != v:
            graph[u].append(v)
    
    cycle = find_cycle(graph, n)
    
    if cycle:
        print("YES")
        print(*cycle[:-1])
    else:
        print("NO")

if __name__ == "__main__":
    main()