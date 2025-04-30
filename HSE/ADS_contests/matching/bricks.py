# Khun algorithm
def dfs(graph, visited, matching, vertex):
    if vertex in visited: return False
    visited.add(vertex)
    for node in graph[vertex]:
        if node not in matching or dfs(graph, visited, matching, matching[node]):
            matching[node] = vertex
            return True
    return False


def main():
    n, word = int(input()), input()
    cubes = [input() for _ in range(n)]
    graph = {}
    for i, letter in enumerate(word):
        graph[i+1] = []
        for c_i, c_letter in enumerate(cubes):
            if letter in c_letter:
                graph[i+1].append(c_i+1)

    matching = {}
    max_matching = 0
    for i in range(1, n + 1):
        visited = set()
        if dfs(graph, visited, matching, i):
            max_matching += 1
    if max_matching < len(word): print("NO")
    else:
        print("YES")
        result = ["0"] * len(word)
        for cube, pos in matching.items():
            result[pos-1] = str(cube)
        print(" ".join(result))


if __name__ == "__main__":
    main()
