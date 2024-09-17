#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <set>

int diff_time(std::string s, std::string t)
{
    int T1 = (s[6] - '0') * 10 + s[7] - '0' + ((s[3] - '0') * 10 + (s[4] - '0')) * 60 +
             ((s[0] - '0') * 10 + s[1] - '0') * 60 * 60;

    int T2 = (t[6] - '0') * 10 + t[7] - '0' + ((t[3] - '0') * 10 + (t[4] - '0')) * 60 +
             ((t[0] - '0') * 10 + t[1] - '0') * 60 * 60;

    if (T2 >= T1) return (T2 - T1) / 60;
    return (24 * 60 * 60 + T2 - T1) / 60;
}

void solve()
{
    std::string start_time;
    std::cin >> start_time;

    int n;
    std::cin >> n;

    std::map<std::pair<std::string, std::string>, int> cannot_solve;
    std::map<std::string, std::pair<int, int>> points;
    std::map<std::string, std::set<std::string>> problems;

    for (int i = 0; i < n; ++i)
    {
        std::string name, time, problem, type;
        std::cin >> name >> time >> problem >> type;
        if (points.count(name) == 0)
        {
            points[name] = {0, 0};
        }
        if (type[0] == 'D' || type[0] == 'F')
        {
            cannot_solve[{name, problem}]++;
        }
        else if (type[0] == 'A')
        {
            if (problems[name].find(problem) == problems[name].end())
            {
                points[name].first++;
                points[name].second += diff_time(start_time, time) + 20 * cannot_solve[{name, problem}];
                problems[name].insert(problem);
            }
        }
    }
    std::vector<std::pair<std::pair<int, int>, std::string>> ans;
    for (auto key: points)
    {
        ans.push_back({{-key.second.first, key.second.second}, {key.first}});
        //std::cout << key.first << " " << key.second.first << " " << key.second.second << std::endl;
    }
    std::sort(ans.begin(), ans.end());
    int place = 1;
    for (int i = 0; i < (int) ans.size(); ++i)
    {
        if (i && (ans[i - 1].first.first != ans[i].first.first || ans[i - 1].first.second != ans[i].first.second))
        {
            place++;
        }
        std::cout << place << " " << ans[i].second << " " << -ans[i].first.first << " " << ans[i].first.second << std::endl;
    }
}

int main()
{
    solve();

    return 0;
}