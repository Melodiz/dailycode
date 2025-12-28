class Solution
{
public:
    int deleteAndEarn(vector<int>& nums)
    {
        int n = nums.size();
        if(n == 0) return 0;
        vector<int> dp(10001, 0);
        for(int i = 0; i < n; i++)
        {
            dp[nums[i]] += nums[i];
        }
        for(int i = 2; i < 10001; i++)
        {
            dp[i] = max(dp[i - 1], dp[i - 2] + dp[i]);
        }
        return dp[10000];
    }
};