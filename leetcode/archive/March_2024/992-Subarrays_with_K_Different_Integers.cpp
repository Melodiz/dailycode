class Solution
{
public:
    int subarraysWithKDistinct(vector<int>& nums, int k)
    {
        int sub_with_max_element_k = subarray_with_atmost_k(nums, k);
        int reduced_sub_with_max_k = subarray_with_atmost_k(nums, k - 1);
        return (sub_with_max_element_k - reduced_sub_with_max_k);
    }
    int subarray_with_atmost_k(vector<int>& nums, int k)
    {
        unordered_map<int, int> data;
        int left = 0, right = 0, ans = 0;
        int n = nums.size()
        while (right < n)
        {
            data[nums[right]]++;
            while (data.size() > k)
            {
                data[nums[left]]--;
                if (data[nums[left]] == 0) data.erase(nums[left]);
                left++;
            }
            ans += right - left + 1;
            right++;
        }
        return ans;
    }
};