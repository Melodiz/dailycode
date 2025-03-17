from collections import deque

def find_diameter(maze, rows, cols):
    # Find any free cell as a starting point
    start = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == '.':
                start = (i, j)
                break
        if start:
            break
    
    if not start:
        return 0  # No free cells
    
    # First BFS to find the farthest node from start
    farthest_node = bfs_farthest(maze, rows, cols, start)
    
    # Second BFS to find the farthest node from the farthest node
    _, max_distance = bfs_with_distance(maze, rows, cols, farthest_node)
    
    return max_distance

def bfs_farthest(maze, rows, cols, start):
    """BFS to find the farthest node from start (without tracking all distances)."""
    queue = deque([start])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    # To track the last node processed (which will be the farthest)
    last_node = start
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Process nodes level by level
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            i, j = queue.popleft()
            last_node = (i, j)
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < rows and 0 <= nj < cols and 
                    maze[ni][nj] == '.' and not visited[ni][nj]):
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    
    return last_node

def bfs_with_distance(maze, rows, cols, start):
    """BFS to find the farthest node and its distance from start."""
    queue = deque([(start, 0)])  # (node, distance)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    farthest_node = start
    max_distance = 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        (i, j), distance = queue.popleft()
        
        if distance > max_distance:
            max_distance = distance
            farthest_node = (i, j)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < rows and 0 <= nj < cols and 
                maze[ni][nj] == '.' and not visited[ni][nj]):
                visited[ni][nj] = True
                queue.append(((ni, nj), distance + 1))
    
    return farthest_node, max_distance

def main():
    cols, rows = map(int, input().split())
    maze = [input() for _ in range(rows)]
    
    max_distance = find_diameter(maze, rows, cols)
    print(max_distance)

if __name__ == "__main__":
    main()