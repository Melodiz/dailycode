def maze_walker(n, m, k, corridors, l, instructions, s):
    from collections import defaultdict

    # Build the graph
    graph = defaultdict(lambda: defaultdict(list))
    for u, v, c in corridors:
        graph[u][c].append(v)

    # Initialize the set of possible rooms
    current_rooms = {s}

    # Process each instruction
    for color in instructions:
        next_rooms = set()
        for room in current_rooms:
            if color in graph[room]:
                next_rooms.update(graph[room][color])
        if not next_rooms:
            return "Hangs"
        current_rooms = next_rooms

    # Output the result
    result_rooms = sorted(current_rooms)
    return f"OK\n{len(result_rooms)}\n" + " ".join(map(str, result_rooms))

def main():
    n, m, k = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        corridors.append((u, v, c))
    l = int(input())
    instructions = list(map(int, input().split()))
    s = int(input())
    print(maze_walker(n, m, k, corridors, l, instructions, s))

if __name__ == "__main__":
    main()