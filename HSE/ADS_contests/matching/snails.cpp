#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

const int INF = 0x3F3F3F3F;

struct Edge {
    int a, b, c, f;
};

class DinicFlow {
private:
    size_t n;
    int s, t;
    std::vector<std::vector<int>> graph;
    std::vector<Edge> edges;
    std::vector<int> d, p, path;
    std::vector<bool> used;
    
    bool bfs() {
        std::queue<int> q;
        d.assign(n, INF);
        d[s] = 0;
        q.push(s);
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int i = 0; i < graph[u].size(); ++i) {
                int id = graph[u][i];
                int v = edges[id].b;

                if (d[v] == INF && edges[id].f < edges[id].c) {
                    d[v] = d[u] + 1;
                    q.push(v);
                }
            }
        }
        return d[t] != INF;
    }
    
    int dfs(int u, int flow) {
        if (u == t || flow == 0) {
            return flow;
        }
        for (; p[u] < graph[u].size(); ++p[u]) {
            int id = graph[u][p[u]];
            int v = edges[id].b;
            if (d[v] == d[u] + 1) {
                int pushed = dfs(v, std::min(flow, edges[id].c - edges[id].f));
                if (pushed) {
                    edges[id].f += pushed;
                    edges[id ^ 1].f -= pushed;
                    return pushed;
                }
            }
        }
        return 0;
    }
    
    void dfs2(int u) {
        path.push_back(u);

        if (u == t) {
            return;
        }

        for (int id : graph[u]) {
            int v = edges[id].b;

            if (!used[id] && edges[id].f == 1) {
                used[id] = true;
                dfs2(v);
                break;
            }
        }
    }

public:
    DinicFlow(size_t vertices, int source, int sink) : n(vertices), s(source), t(sink) {
        graph.resize(n);
        d.resize(n);
        p.resize(n);
    }
    
    void addEdge(int a, int b) {
        graph[a].push_back(edges.size());
        edges.push_back({a, b, 1, 0});
        graph[b].push_back(edges.size());
        edges.push_back({b, a, 0, 0});
    }
    
    int maxFlow() {
        int flow = 0;
        while (bfs()) {
            p.assign(n, 0);
            int f = dfs(s, INF);
            while (f) {
                flow += f;
                f = dfs(s, INF);
            }
        }
        return flow;
    }
    
    void printPath() {
        dfs2(s);

        for (int i : path) {
            std::cout << i + 1 << " ";
        }
        std::cout << "\n";

        path.clear();
    }
    
    void resetUsed() {
        used.assign(edges.size(), false);
    }
};

int main() {
    size_t n, m;
    int s, t;
    
    std::cin >> n >> m;
    std::cin >> s >> t;
    s--; t--;
    
    DinicFlow flow(n, s, t);
    
    for (int i = 0; i < m; ++i) {
        int ai, bi;
        std::cin >> ai >> bi;
        ai--; bi--;
        flow.addEdge(ai, bi);
    }

    int maxFlow = flow.maxFlow();

    if (maxFlow < 2) {
        std::cout << "NO";
    } else {
        std::cout << "YES\n";
        flow.resetUsed();
        flow.printPath();
        flow.printPath();
    }
    return 0;
}