#include <algorithm>
#include <iostream>
#include <vector>

bool isPossible(const std::vector<std::pair<size_t, bool>>& data, size_t capacity)
{
    // Sort the data by time, and in case of tie, by type (start before end)
    std::vector<std::pair<size_t, bool>> sorted_data = data;
    std::sort(sorted_data.begin(), sorted_data.end(), [](const std::pair<size_t, bool>& a, const std::pair<size_t, bool>& b) {
        return a.first == b.first ? a.second > b.second : a.first < b.first;
    });

    size_t current_overlaps = 0;

    for (const auto& point: sorted_data)
    {
        if (point.second)
        {// start of a line
            current_overlaps++;
            if (current_overlaps > capacity)
            {
                return false;
            }
        }
        else
        {// end of a line
            current_overlaps--;
        }
    }

    return true;
}

std::vector<std::pair<size_t, bool>> add_end_points(const std::vector<std::pair<size_t, bool>>& data, size_t value)
{
    std::vector<std::pair<size_t, bool>> new_data;
    new_data.reserve(data.size() * 2); // Reserve memory to avoid multiple allocations
    for (const auto& point: data)
    {
        new_data.push_back(point);
        if (point.second)
        {
            new_data.emplace_back(point.first + value, false);
        }
    }
    return new_data;
}

std::string binary_search(const std::vector<std::pair<size_t, bool>>& data, size_t capacity)
{
    size_t left = 0, right = static_cast<size_t>(1) << 31;
    size_t upper = right;

    while (left < right)
    {
        size_t mid = (left + right) >> 1;
        std::vector<std::pair<size_t, bool>> new_data = add_end_points(data, mid);
        if (isPossible(new_data, capacity))
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }

    if (left == 0)
    {
        return "Impossible";
    }
    if (left == upper)
    {
        return "INF";
    }
    return std::to_string(left);
}

int main()
{
    size_t n, capacity;
    std::cin >> n >> capacity;
    std::vector<std::pair<size_t, bool>> data(n);
    for (size_t i = 0; i < n; ++i)
    {
        size_t time;
        std::cin >> time;
        data[i] = {time, true};
    }
    std::cout << binary_search(data, capacity) << std::endl;
    return 0;
}