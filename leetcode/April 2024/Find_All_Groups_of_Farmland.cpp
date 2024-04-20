class Solution
{
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land)
    {
        int m = land.size();
        int n = land[0].size();
        vector<vector<int>> ans;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (land[i][j] == 1)
                {
                    ans.push_back({i, j});
                }
            }
        }
        return ans;
    }
};