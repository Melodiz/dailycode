#include <iostream>
#include <vector>
#include <algorithm>

int solver(std::vector<std::vector<int>>& data, int ans)
{
    int start = data[0][1];
    int end = data[0][0];
    bool flag = false;
    // remove all intersections;
    std::vector<std::vector<int>> new_data;
    if (data.size() <= 1) { return ans + 1; }
    for (int i = 1; i < data.size(); ++i)
    {
        if (data[i][0] == 0 || data[i][1] == 0 || data[i][1] <= end) { continue; }
        else { new_data.push_back(data[i]); }
    }
    if (new_data.size() > 0) { return solver(new_data, ans + 1); }
    return ans + 1;
}

int main()
{
    int n, k, m;
    std::cin >> n;
    std::vector<std::vector<int>> data;

    for (int iter = 0; iter < n; ++iter)
    {
        std::cin >> k >> m;
        data.push_back({m, k});
    }
    std::sort(data.begin(), data.end());
    std::cout << solver(data, 0) << std::endl;
    return 0;
}