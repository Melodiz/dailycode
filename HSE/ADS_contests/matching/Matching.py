# Khun algorithm
def dfs(graph, visited, matching, vertex):
    for node in graph[vertex]:
        if node not in visited:
            visited.add(node)
            if node not in matching or dfs(graph, visited, matching, matching[node]):
                matching[node] = vertex
                return True
    return False

def main():
    n, _ = map(int, input().split())
    graph = [[]]+[list(map(int, input().split()))[:-1] for _ in range(n)]
    
    matching = {}
    max_matching = 0
    for i in range(1, n + 1):
        visited = set()
        if dfs(graph, visited, matching, i):
            max_matching += 1

    print(max_matching)
    for v, u in matching.items():
        print(u, v)


if __name__ == "__main__":
    main()
