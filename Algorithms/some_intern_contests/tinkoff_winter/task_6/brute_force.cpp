#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

typedef pair<int, int> Point;

bool is_non_degenerate(const Point& p1, const Point& p2, const Point& p3) {
    return (p2.first - p1.first) * (p3.second - p1.second) != 
           (p3.first - p1.first) * (p2.second - p1.second);
}

int backtrack(int index, set<int>& used_points, int count, 
              const vector<vector<int>>& valid_triangles) {
    if (index == valid_triangles.size()) {
        return count;
    }
    
    // Try including the current triangle
    const auto& current_triangle = valid_triangles[index];
    bool can_include = true;
    for (int point : current_triangle) {
        if (used_points.find(point) != used_points.end()) {
            can_include = false;
            break;
        }
    }
    
    int include = 0;
    if (can_include) {
        set<int> new_used_points = used_points;
        for (int point : current_triangle) {
            new_used_points.insert(point);
        }
        include = backtrack(index + 1, new_used_points, count + 1, valid_triangles);
    }
    
    // Try excluding the current triangle
    int exclude = backtrack(index + 1, used_points, count, valid_triangles);
    
    return max(include, exclude);
}

int solve(int n, const vector<Point>& points) {
    vector<vector<int>> all_triangles;
    for (int i = 0; i < n - 2; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            for (int k = j + 1; k < n; ++k) {
                all_triangles.push_back({i, j, k});
            }
        }
    }
    
    
    vector<vector<int>> valid_triangles;
    for (const auto& triangle : all_triangles) {
        if (is_non_degenerate(points[triangle[0]], points[triangle[1]], points[triangle[2]])) {
            valid_triangles.push_back(triangle);
        }
    }
    
    set<int> used_points;
    return backtrack(0, used_points, 0, valid_triangles);
}

int main() {
    int n;
    cin >> n;
    
    vector<Point> points(n);
    for (int i = 0; i < n; ++i) {
        cin >> points[i].first >> points[i].second;
    }
    
    cout << solve(n, points) << endl;
    
    return 0;
}