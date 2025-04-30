#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <climits>
using namespace std;

int MaxFlowMinCut(int n, int m, int w, int b, int g, vector<string>& grid) {
    int s = 0;
    int t = n * m + 1;
    
    vector<vector<int>> graph(n * m + 2);
    map<pair<int, int>, int> capacities;
    
    auto get_node = [m](int i, int j) {
        return i * m + j + 1;
    };
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int node = get_node(i, j);
            
            if (grid[i][j] == 'B') {
                graph[s].push_back(node);
                graph[node].push_back(s);
                capacities[{s, node}] = w;
                capacities[{node, s}] = 0;
            } else {
                graph[node].push_back(t);
                graph[t].push_back(node);
                capacities[{node, t}] = b;
                capacities[{t, node}] = 0;
            }
            
            if (j + 1 < m) {
                int neighbor = get_node(i, j + 1);
                graph[node].push_back(neighbor);
                graph[neighbor].push_back(node);
                capacities[{node, neighbor}] = g;
                capacities[{neighbor, node}] = g;
            }
            
            if (i + 1 < n) {
                int neighbor = get_node(i + 1, j);
                graph[node].push_back(neighbor);
                graph[neighbor].push_back(node);
                capacities[{node, neighbor}] = g;
                capacities[{neighbor, node}] = g;
            }
        }
    }
    
    auto bfs = [&]() -> map<int, int> {
        vector<bool> visited(n * m + 2, false);
        visited[s] = true;
        queue<int> q;
        q.push(s);
        map<int, int> parent;
        
        while (!q.empty() && !visited[t]) {
            int current = q.front();
            q.pop();
            
            for (int neighbor : graph[current]) {
                if (!visited[neighbor] && capacities[{current, neighbor}] > 0) {
                    visited[neighbor] = true;
                    parent[neighbor] = current;
                    q.push(neighbor);
                }
            }
        }
        
        if (visited[t]) {
            return parent;
        }
        return map<int, int>();
    };
    
    int max_flow = 0;
    while (true) {
        map<int, int> parent = bfs();
        if (parent.empty()) {
            break;
        }
        
        int current = t;
        int path_flow = INT_MAX;
        while (current != s) {
            int prev = parent[current];
            path_flow = min(path_flow, capacities[{prev, current}]);
            current = prev;
        }
        
        current = t;
        while (current != s) {
            int prev = parent[current];
            capacities[{prev, current}] -= path_flow;
            capacities[{current, prev}] += path_flow;
            current = prev;
        }
        
        max_flow += path_flow;
    }
    
    return max_flow;
}

int main() {
    int n, m, w, b, g;
    cin >> n >> m >> w >> b >> g;
    
    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }
    
    cout << MaxFlowMinCut(n, m, w, b, g, grid) << endl;
    
    return 0;
}