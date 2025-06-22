#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <limits.h>

struct Child {
    int x, y;
    Child(int x, int y) : x(x), y(y) {}
};

struct Delivery {
    int x, y, capacity;
    Delivery(int x, int y, int capacity) : x(x), y(y), capacity(capacity) {}
};

std::vector<int> bfs(const std::vector<std::vector<int>>& capacityGraph, int source, int sink) {
    int n = capacityGraph.size();
    std::vector<int> parent(n, -1);
    std::queue<int> q;
    q.push(source);
    parent[source] = source;
    while (!q.empty() && parent[sink] == -1) {
        int u = q.front();
        q.pop();
        for (int v = 0; v < n; ++v) {
            if (parent[v] == -1 && capacityGraph[u][v] > 0) {
                parent[v] = u;
                q.push(v);
            }
        }
    }
    return parent;
}

bool canDeliverWithinDistance(std::vector<Child>& children, std::vector<Delivery>& deliveries, double maxDist) {
    int numChildren = children.size();
    int numDeliveries = deliveries.size();
    
    std::vector<std::vector<int>> capacityGraph(numChildren + numDeliveries + 2, std::vector<int>(numChildren + numDeliveries + 2, 0));
    int source = numChildren + numDeliveries;
    int sink = numChildren + numDeliveries + 1;

    for (int i = 0; i < numChildren; ++i) {
        capacityGraph[source][i] = 1;
    }

    for (int i = 0; i < numDeliveries; ++i) {
        capacityGraph[numChildren + i][sink] = deliveries[i].capacity;
    }

    for (int i = 0; i < numChildren; ++i) {
        for (int j = 0; j < numDeliveries; ++j) {
            double dist = std::sqrt(std::pow(children[i].x - deliveries[j].x, 2) + std::pow(children[i].y - deliveries[j].y, 2));
            if (dist <= maxDist) {
                capacityGraph[i][numChildren + j] = 1;
            }
        }
    }

    int maxFlow = 0;
    std::vector<int> parent;
    while ((parent = bfs(capacityGraph, source, sink))[sink] != -1) {
        int flow = INT_MAX;
        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            flow = std::min(flow, capacityGraph[u][v]);
        }
        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            capacityGraph[u][v] -= flow;
            capacityGraph[v][u] += flow;
        }
        maxFlow += flow;
    }

    return maxFlow == numChildren;
}

int main() {
    std::ios::sync_with_stdio(false), std::cin.tie(0), std::cout.tie(0);
    std::cout.setf(std::ios::fixed), std::cout.precision(7);
    int numChildren, numDeliveries;
    std::cin >> numChildren >> numDeliveries;

    std::vector<Child> children;
    for (int i = 0; i < numChildren; ++i) {
        int x, y;
        std::cin >> x >> y;
        children.emplace_back(x, y);
    }

    std::vector<Delivery> deliveries;
    for (int i = 0; i < numDeliveries; ++i) {
        int x, y, capacity;
        std::cin >> x >> y >> capacity;
        deliveries.emplace_back(x, y, capacity);
    }

    double low = 0;
    double high = 1e6;
    double result = high;

    while (high - low > 1e-6) {
        double mid = (low + high) / 2;
        if (canDeliverWithinDistance(children, deliveries, mid)) {
            result = mid;
            high = mid;
        } else {
            low = mid;
        }
    }

    std::cout << result << std::endl;

    return 0;
}