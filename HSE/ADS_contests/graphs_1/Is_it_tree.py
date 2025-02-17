from collections import defaultdict

def iterative_dfs(graph, start, visited):
    stack = [start]
    visited_count = 0
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            visited_count += 1
            stack.extend(neighbor for neighbor in graph[vertex] if not visited[neighbor])
    return visited_count

def is_tree(n, edges):
    # Check if number of edges is n-1
    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    
    # Check if the graph is connected
    visited_count = iterative_dfs(graph, 1, visited)
    
    return visited_count == n

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    if is_tree(n, edges):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()