#include <iostream>
#include <vector>
#include <limits>

int solve(int n) {
    const long long INF = std::numeric_limits<long long>::max();
    std::vector<long long> dist(n + 1, INF);
    dist[1] = 0;
    
    auto weight = [](int i, int j) -> int {
        return (179 * i + 719 * j) % 1000 - 500;
    };
    
    for (int i = 1; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            if (dist[i] != INF && dist[i] + weight(i, j) < dist[j]) {
                dist[j] = dist[i] + weight(i, j);
            }
        }
    }
    
    return dist[n];
}

int main() {
    int n;
    std::cin >> n;
    std::cout << solve(n) << std::endl;
    return 0;
}