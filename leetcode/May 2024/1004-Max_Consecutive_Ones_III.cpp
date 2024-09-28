class Solution
{
public:
    int longestOnes(vector<int>& nums, int k)
    {
        int left = 0, right = 0;
        int zeroCount = 0;
        int maxLen = 0;
        while (right < nums.size())
        {
            if (nums[right] == 0)
                zeroCount++;
            while(zeroCount > k)
            {
                if (nums[left] == 0)
                    zeroCount--;
                left++;
            }
            // now zeroCount <= k, so maxLen = right - left + 1
            maxLen = max(maxLen, right - left + 1);
            right++; // move right
        }
        return maxLen;
    }
};