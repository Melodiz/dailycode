def read_connectivity_matrix():
    n, s = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]
    return matrix, s


def dfs(start, connectivity):
    visited = [False] * len(connectivity)
    stack = [start]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in range(len(connectivity)):
                if connectivity[vertex][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
    return visited


def main():
    connectivity, start = read_connectivity_matrix()
    visited = dfs(start-1, connectivity)
    print(sum(visited))


if __name__ == "__main__":
    main()