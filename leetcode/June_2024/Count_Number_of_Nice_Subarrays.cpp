class Solution
{
public:
    int numberOfSubarrays(vector<int>& nums, int k)
    {
        int n = nums.size();
        vector<int> prefix(n + 1, 0);
        int count = 0, result = 0;
        
        prefix[0] = 1; // Base case: there's one way to have zero odd numbers
        
        for (int i = 0; i < n; i++)
        {
            if (nums[i] % 2 == 1)
                count++;
            
            if (count >= k)
                result += prefix[count - k];
            
            prefix[count]++;
        }
        
        return result;
    }
};