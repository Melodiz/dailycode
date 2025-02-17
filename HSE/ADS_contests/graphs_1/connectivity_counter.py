from collections import defaultdict

def iterative_dfs(graph, start, visited, component):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            component.append(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if not visited[neighbor])

def find_connected_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    components = []
    
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            component = []
            iterative_dfs(graph, vertex, visited, component)
            components.append(component)
    
    return components

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    components = find_connected_components(n, edges)

    component_mapping = [0] * (n + 1)
    for i, component in enumerate(components, 1):
        for vertex in component:
            component_mapping[vertex] = i

    print(len(components))
    print(*component_mapping[1:])

if __name__ == "__main__":
    main()