def dfs(graph, start, visited):
    visited.add(start)
    stack = []

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

def bfs(graph, start):
    queue = [start]
    visited = set()

    while queue:
        current = queue.pop(0)
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited


def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]


import heapq
def djikstra(graph, start):
    queue = [(0, start)]
    distances = [float('inf')] * len(graph)
    visited = set()

    distances[start] = 0
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited: continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


def bellman_ford(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                distance = distances[node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    for node in graph:
        for neighbor, weight in graph[node].items():
            distance = distances[node] + weight
            if distance < distances[neighbor]:
                return "Graph contains negative weight cycle"

    return distances


def floyd_warshall(graph):
    num_vertices = len(graph)
    distances = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        distances[i][i] = 0

    # Initialize the distances matrix with given edges
    for edge in graph:
        distances[edge[0]][edge[1]] = edge[2]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances


def A_star(graph, start, end):
    def h(node, end):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    dists = [float('inf')] * len(graph)
    dists[start] = 0
    visited = set()
    queue = [(0, start)]
    while queue:
        curr_node, curr_dist = heapq.heappop(queue)
        if curr_node == end:
            return dists
        if curr_node in visited:
            continue
        visited.add(curr_node)
        for neighbor, weight in graph[curr_node].items():
            tentative_dist = curr_dist + weight
            if tentative_dist < dists[neighbor]:
                dists[neighbor] = tentative_dist
                heapq.heappush(queue, (tentative_dist + h(neighbor, end), neighbor))
    return None

def prims(graph, start):
    visited = set()
    queue = [(0, start)]
    total_weight = 0

    while queue:
        current_weight, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        total_weight += current_weight
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (weight, neighbor))

    return total_weight

def kruskal(graph):
    edges = [(weight, u, v) for u, v, weight in graph]
    edges.sort()
    parent = list(range(len(graph)))
    total_weight = 0

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        parent1 = find(node1)
        parent2 = find(node2)
        if parent1 != parent2:
            parent[parent1] = parent2

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_weight += weight

    return total_weight

def Edmond_Carp(graph, source, sink):
    max_flow = 0
    while True:
        path = bfs(graph, source)
        if not path:
            break
        flow = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            flow = min(flow, graph[u][v])
        max_flow += flow

        for u, v in path:
            graph[u][v] -= flow
            graph[v][u] += flow

    return max_flow

def Ford_Fulkerson_dfs(graph, source, sink):
    visited = set()
    max_flow = 0

    def dfs(node):
        if node == sink:
            return float('inf')
        visited.add(node)
        for neighbor, capacity in graph[node].items():
            if neighbor not in visited and capacity > 0:
                path_flow = dfs(neighbor)
                if path_flow > 0:
                    graph[node][neighbor] -= path_flow
                    graph[neighbor][node] += path_flow
                    return path_flow
        return 0

    while True:
        visited.clear()
        path_flow = dfs(source)
        if path_flow == 0:
            break
        max_flow += path_flow

    return max_flow


def Kuhn(graph):
    num_vertices = len(graph)
    matching = [-1] * num_vertices
    visited = [False] * num_vertices

    def dfs(node):
        if visited[node]:
            return False
        visited[node] = True
        for neighbor in graph[node]:
            if matching[neighbor] == -1 or dfs(matching[neighbor]):
                matching[neighbor] = node
                return True
        return False

    for node in range(num_vertices):
        if dfs(node):
            break

    return matching

