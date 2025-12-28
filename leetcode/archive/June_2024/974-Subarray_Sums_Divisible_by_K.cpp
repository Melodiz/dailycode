class Solution
{
public:
    int subarraysDivByK(vector<int>& nums, int k)
    {
        int res = 0;
        unordered_map<int, int> m;
        m[0] = 1;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            sum = (sum + nums[i]) % k;
            if (sum < 0)
                sum += k;
            res += m[sum];
            m[sum]++;
        }
        return res;
    }
};