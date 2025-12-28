#include <iostream>
#include <map>
using namespace std;
class Solution
{
public:
    long long countSubarrays(vector<int>& nums, int k)
    {
        int val = *max_element(nums.begin(), nums.end());
        long long ans = 0;
        int n = nums.size();

        int l = 0, r = 0;
        while (r < n)
        {
            k -= (nums[r++] == val);
            while (k == 0)
            {
                k += (nums[l++] == val);
            }
            ans += l;
        }
        return ans;
    }
};