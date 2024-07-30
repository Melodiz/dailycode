#include <map>
class Solution
{
public:
    int maxSubarrayLength(vector<int> &nums, int k)
    {
        map<int, int> data;
        int ans = 0;
        int l = 0;
        for (int r = 0; r < nums.size(); r++)
        {
            data[nums[r]]++;
            if (data[nums[r]] > k)
            {
                while (data[nums[l]] != data[nums[r]])
                {
                    data[nums[l]]--;
                    l++;
                }
                data[nums[l]]--;
                l++;
                if (ans < r-l+1){}
            }
            ans = std::max(ans, r-l+1);
        }
        return ans;
    }
};