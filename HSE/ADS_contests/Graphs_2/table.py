from collections import deque

def main():
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    
    distance = [[float('inf')] * m for _ in range(n)]
    queue = deque()
    
    # Add all cells with 1 to the queue and set their distance to 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                distance[i][j] = 0
                queue.append((i, j))
    
    # BFS to find minimum distances
    while queue:
        i, j = queue.popleft()
        
        # Check all four paths
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < n and 0 <= nj < m:
                # If we found a shorter path to the cell
                if distance[ni][nj] > distance[i][j] + 1:
                    distance[ni][nj] = distance[i][j] + 1
                    queue.append((ni, nj))
    
    for row in distance:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()