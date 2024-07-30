class Solution
{
public:
    int specialArray(vector<int>& nums)
    {
        // Count the number of elements greater than or equal to x for each x in the range [0, nums.length].
        // If for any x, the condition satisfies, return that x. Otherwise, there is no answer.
        int n = nums.size();
        vector<int> count(n + 1, 0);
        for (int i = 0; i < n; i++)
        {
            if (nums[i] <= n) { count[nums[i]] = INT_MIN;}
            int upper_bound = min(n, nums[i]);
            for (int j = upper_bound; j >= 0; j--){count[j]++;}
        }
        for (int i = 0; i <= n; i++)
        {
            if (count[i] == i) return i;
        }
        return -1;
    }
};