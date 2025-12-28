#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums)
    {
        vector<pair<int, int>> mapped_nums;
        for (int num: nums)
        {
            string mapped_num = "";
            for (char digit: to_string(num))
            {
                mapped_num += to_string(mapping[digit - '0']);
            }
            mapped_nums.push_back(make_pair(stoi(mapped_num), num));
        }
        // sort mapped_nums based only on the first element
        sort(mapped_nums.begin(), mapped_nums.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first < b.first;
        });
        vector<int> sorted_nums;
        for (auto& pair: mapped_nums)
        {
            std::cout << pair.second << " -> " << pair.first << endl;// Debugging purpose
            sorted_nums.push_back(pair.second);
        }
        return sorted_nums;
    }
};