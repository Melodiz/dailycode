class Solution
{
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries)
    {
        int n = arr.size();
        vector<int> prefixXor(n + 1, 0);
        
        for (int i = 1; i <= n; ++i)
            prefixXor[i] = prefixXor[i - 1] ^ arr[i - 1];
        
        vector<int> result;
        for (const auto& query : queries)
        {
            int left = query[0];
            int right = query[1];
            result.push_back(prefixXor[right + 1] ^ prefixXor[left]);
        }
        
        return result;
    }
};