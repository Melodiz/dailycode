#include <algorithm> // copy
#include <iostream>  // boolalpha, cin, cout, streamsize
#include <iterator>  // back_inserter, istream_iterator, ostream_iterator, prev
#include <limits>    // numeric_limits
#include <sstream>   // istringstream
#include <string>    // getline, string
#include <vector>    // vector

int main()
{
    std::deque<int> max_indices;
    std::vector<int> res;
    std::vector<int> data;
    unsigned long length, gap;
    int number;

    std::cin >> length >> gap;

    while (std::cin >> number)
    {
        data.push_back(number);
    }
    for (int i = 0; i < nums.size(); i++)
    {
        while (!max_indices.empty() && nums[max_indices.back()] <= nums[i])
        {
            max_indices.pop_back();
        }
        max_indices.push_back(i);
        // remove first element if it's outside the window
        if (max_indices.front() == i - k)
        {
            max_indices.pop_front();
        }
        // if window has k elements add to results (first k-1 windows have < k elements because we start from empty
        // window and add 1 element each iteration)
        if (i >= k - 1)
        {
            res.emplace_back(nums[max_indices.front()]);
        }
    }
}
