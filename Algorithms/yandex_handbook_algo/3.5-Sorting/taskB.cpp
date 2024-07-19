#include <deque>
#include <iostream>
#include <vector>

std::vector<int> mergeSorted(std::vector<std::deque<int>>& data)
{
    std::vector<int> result;
    bool flag = true;
    while (flag)
    {
        int cur_min = INT_MAX;
        int min_index = -1; // Initialize to an invalid index
        flag = false;
        for (int i = 0; i < data.size(); ++i)
        {
            if (!data[i].empty())
            {
                flag = true;
                if (cur_min > data[i].front())
                {
                    cur_min = data[i].front();
                    min_index = i;
                }
            }
        }
        if (min_index != -1) // Ensure min_index is valid
        {
            result.push_back(cur_min);
            data[min_index].pop_front();
        }
    }
    return result;
}

int main()
{
    int n, k, p;
    std::cin >> n;
    std::vector<std::deque<int>> data;
    for (size_t epos = 0; epos < n; ++epos)
    {
        std::cin >> k;
        std::deque<int> dq;
        for (size_t i = 0; i < k; ++i)
        {
            std::cin >> p;
            dq.push_back(p);
        }
        data.push_back(dq);
    }
    std::vector<int> result = mergeSorted(data);
    for (size_t i = 0; i < result.size(); ++i)
    {
        std::cout << result[i] << ' ';
    }

    return 0;
}