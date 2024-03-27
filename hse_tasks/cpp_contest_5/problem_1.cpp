#include <deque>
#include <iostream>
#include <vector>

int main()
{
    int window, n;
    std::cin >> n >> window;

    std::deque<int> deq;
    std::vector<int> res;

    // reading data
    int nums[n];
    int temp;
    for (int i = 0; i < n; i++)
    {
        std::cin >> temp;
        nums[i] = temp;
    }

    // algorithm
    for (int i = 0; i < n; i++)
    {
        while (!deq.empty() && nums[deq.back()] >= nums[i])
        {
            deq.pop_back();
        }
        deq.push_back(i);
        if (deq.front() == i - window)
        {
            deq.pop_front();
        }
        if (i >= window - 1)
        {
            res.emplace_back(nums[deq.front()]);
        }
    }

    // print data
    for (size_t i = 0; i < res.size(); i++)
    {
        std::cout << res[i] << std::endl;
    }

    return 0;
}
