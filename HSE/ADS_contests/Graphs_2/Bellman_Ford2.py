def solve(n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0  
    
    def weight(i, j):
        return (179 * i + 719 * j) % 1000 - 500
    
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if dist[i] != INF and dist[j] > dist[i] + weight(i, j):
                dist[j] = dist[i] + weight(i, j)
    
    return dist[n]

if __name__ == "__main__":
    n = int(input())
    print(solve(n))