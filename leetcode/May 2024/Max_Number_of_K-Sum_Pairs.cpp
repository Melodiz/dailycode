class Solution
{
public:
    int maxOperations(vector<int>& nums, int k)
    {
        unordered_map<int, int> freq;
        for (int num: nums)
        {
            freq[num]++;
        }

        int ans = 0;
        for (auto it = freq.begin(); it != freq.end(); ++it)
        {
            int num = it->first;
            int complement = k - num;
            // Avoid double counting
            if (complement > num) continue;

            if (num == complement)
            {
                ans += it->second / 2;
            }
            else if (freq.find(complement) != freq.end())
            {
                int minOperations = min(it->second, freq[complement]);
                ans += minOperations;
                // Update the counts to avoid double counting in future iterations
                freq[num] -= minOperations;
                freq[complement] -= minOperations;
            }
        }

        return ans;
    }
};