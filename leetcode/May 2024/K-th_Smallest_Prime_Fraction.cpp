#include <vector>
#include <map>
#include <algorithm>

class Solution
{
public:
    std::vector<int> kthSmallestPrimeFraction(std::vector<int>& arr, int k)
    {
        std::vector<double> results;
        std::map<double, std::vector<int>> data;

        for (int i = 0; i < arr.size(); ++i)
        {
            for (int j = i + 1; j < arr.size(); ++j)
            {
                double fraction = static_cast<double>(arr[i]) / arr[j];
                data[fraction] = {arr[i], arr[j]};
                results.push_back(fraction);
            }
        }
        std::sort(results.begin(), results.end());
        return data[results[k - 1]];
    }
};