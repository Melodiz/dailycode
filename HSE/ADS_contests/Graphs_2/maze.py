from collections import deque

def solve(n, m, maze, x1, y1, x2, y2):
    
    # BFS to find shortest path
    queue = deque([(x1, y1, 0)]) 
    visited = set([(x1, y1)])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        # If we reached home
        if x == x2 and y == y2:
            return dist
        
        # Try all four directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is valid
            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))
    
    return -1

def main():
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    
    # Read start and end positions
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    # Convert to 0-indexed
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    print(solve(n, m, maze, x1, y1, x2, y2))

if __name__ == "__main__":
    main()