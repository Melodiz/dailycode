#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <utility>

using namespace std;

const long long INF = 2009000999;

vector<long long> dijkstra(const vector<vector<pair<int, int>>>& graph, int start, int n) {
    vector<long long> distances(n, INF);
    distances[start] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});
    
    vector<bool> visited(n, false);
    
    while (!pq.empty()) {
        int current_vertex = pq.top().second;
        long long current_distance = pq.top().first;
        pq.pop();
        
        if (visited[current_vertex]) {
            continue;
        }
        
        visited[current_vertex] = true;
        
        for (const auto& edge : graph[current_vertex]) {
            int neighbor = edge.first;
            int weight = edge.second;
            
            if (visited[neighbor]) {
                continue;
            }
            
            long long distance = current_distance + weight;
            
            if (distance < distances[neighbor]) {
                distances[neighbor] = distance;
                pq.push({distance, neighbor});
            }
        }
    }
    
    return distances;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int num_tests;
    cin >> num_tests;
    
    for (int test = 0; test < num_tests; ++test) {
        int n, m;
        cin >> n >> m;
        
        // Initialize graph as adjacency list
        vector<vector<pair<int, int>>> graph(n);
        
        for (int i = 0; i < m; ++i) {
            int u, v, w;
            cin >> u >> v >> w;
            
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }
        
        // // Process duplicate edges
        // for (int i = 0; i < n; ++i) {
        //     if (graph[i].empty()) continue;
            
        //     // Sort edges by neighbor
        //     sort(graph[i].begin(), graph[i].end());
            
        //     // Remove duplicates keeping minimum weight
        //     vector<pair<int, int>> unique_edges;
        //     unique_edges.push_back(graph[i][0]);
            
        //     for (size_t j = 1; j < graph[i].size(); ++j) {
        //         if (graph[i][j].first == unique_edges.back().first) {
        //             // Same neighbor, keep minimum weight
        //             unique_edges.back().second = min(unique_edges.back().second, graph[i][j].second);
        //         } else {
        //             unique_edges.push_back(graph[i][j]);
        //         }
        //     }
            
        //     graph[i] = std::move(unique_edges);
        // }
        
        int start;
        cin >> start;
        
        // Run Dijkstra's algorithm
        vector<long long> distances = dijkstra(graph, start, n);
        
        // Print distances
        for (int i = 0; i < n; ++i) {
            cout << distances[i];
            if (i < n - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }
    
    return 0;
}