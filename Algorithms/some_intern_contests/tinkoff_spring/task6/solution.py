from collections import deque, defaultdict

def find_min_time(n, processes):
    # Построение графа зависимостей и вычисление входящих степеней
    graph = defaultdict(list)
    in_degree = [0] * n
    execution_time = [0] * n
    
    for i in range(n):
        data = processes[i]
        t_i = data[0]
        execution_time[i] = t_i
        dependencies = data[1:]
        for dep in dependencies:
            graph[dep - 1].append(i)
            in_degree[i] += 1
    
    # Топологическая сортировка
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    min_time = [0] * n
    
    while queue:
        process = queue.popleft()
        for neighbor in graph[process]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            min_time[neighbor] = max(min_time[neighbor], min_time[process] + execution_time[process])
    
    # Вычисление минимального времени завершения всех процессов
    result = 0
    for i in range(n):
        result = max(result, min_time[i] + execution_time[i])
    
    return result

def main():
    n = int(input())
    processes = []
    for _ in range(n):
        data = list(map(int, input().split()))
        processes.append(data)
    
    print(find_min_time(n, processes))

if __name__ == "__main__":
    main()