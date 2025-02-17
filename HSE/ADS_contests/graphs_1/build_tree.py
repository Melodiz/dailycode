import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(node, parent, graph):
    max_depth = 0
    for child in graph[node]:
        if child != parent:
            depth = dfs(child, node, graph)
            max_depth = max(max_depth, depth)
    return max_depth + 1

def find_longest_path(graph, n):
    _, end1 = max((dfs(node, -1, graph), node) for node in range(1, n+1))
    
    longest_path = dfs(end1, -1, graph)
    
    return longest_path

def main():
    n = int(input())
    graph = defaultdict(list)
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    result = find_longest_path(graph, n)
    print(result)

if __name__ == "__main__":
    main()