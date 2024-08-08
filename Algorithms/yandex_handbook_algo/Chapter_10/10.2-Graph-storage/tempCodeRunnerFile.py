def count_visited_cells(n, m, room, start_r, start_c, actions):
    # Directions: 0 = up, 1 = right, 2 = down, 3 = left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0  # Initially facing up

    # Starting position
    r, c = start_r, start_c

    # Set to keep track of visited cells
    visited = set()
    visited.add((r, c))

    for action in actions:
        if action == 'L':
            direction = (direction - 1) % 4
        elif action == 'R':
            direction = (direction + 1) % 4
        elif action == 'M':
            new_r = r + directions[direction][1]
            new_c = c + directions[direction][0]
            if 0 <= new_r < n and 0 <= new_c < m and room[new_r][new_c] == '.':
                r, c = new_r, new_c
                visited.add((r, c))

    return len(visited)

n, m = map(int, input().split())
room = [list(input()) for _ in range(n)]
start_r, start_c = map(int, input().split())
q = int(input())
actions = list(input())

print(count_visited_cells(n, m, room, start_r-1, start_c-1, actions))