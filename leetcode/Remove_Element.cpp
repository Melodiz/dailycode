class Solution
{
public:
    int removeElement(vector<int>& nums, int val)
    {
        size_t k = 0;
        for (size_t i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] == val)
            {
                swap(nums[i], nums[i + 1]);
                k++;
            }
        }
        for (size_t i = 0; i < k-1; i++)
        {
            nums.pop_back();
        }
        return nums.size();
    }
};