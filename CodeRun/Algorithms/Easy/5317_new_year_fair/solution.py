# Solution for https://coderun.yandex.ru/problem/new-year-fair
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/CodeRun

def main():
    n, m = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * (n + 1)
    number_of_connected_components = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            number_of_connected_components += 1
            stack = [i]
            visited[i] = True
            while stack:
                current = stack.pop()
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
    
    print(m - n + number_of_connected_components)
    return 0

if __name__ == "__main__":
    main()