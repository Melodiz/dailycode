#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXN = 300;
const long long INF = 1e18;

struct Point {
    long long x, y;
};

vector<Point> points;
int n;
bool used[MAXN];
int matching[MAXN];
long long dist[MAXN][MAXN];

bool is_collinear(const Point& a, const Point& b, const Point& c) {
    return (b.y - a.y) * (c.x - b.x) == (c.y - b.y) * (b.x - a.x);
}

long long squared_dist(const Point& a, const Point& b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

bool try_kuhn(int v) {
    if (used[v]) return false;
    used[v] = true;
    for (int to = 0; to < n; ++to) {
        if (matching[to] == -1 || try_kuhn(matching[to])) {
            matching[to] = v;
            return true;
        }
    }
    return false;
}

int main() {
    cin >> n;
    points.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> points[i].x >> points[i].y;
    }

    // Precalculate distances
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            dist[i][j] = squared_dist(points[i], points[j]);
        }
    }

    int max_groups = 0;
    vector<bool> used_points(n, false);

    for (int i = 0; i < n; ++i) {
        if (used_points[i]) continue;
        for (int j = i + 1; j < n; ++j) {
            if (used_points[j]) continue;
            for (int k = j + 1; k < n; ++k) {
                if (used_points[k]) continue;
                if (!is_collinear(points[i], points[j], points[k])) {
                    used_points[i] = used_points[j] = used_points[k] = true;
                    max_groups++;
                    break;
                }
            }
            if (used_points[j]) break;
        }
    }

    cout << max_groups << endl;

    return 0;
}