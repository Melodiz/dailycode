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
    void dfs(vector<vector<int>>& land, vector<vector<int>>& ans, int i, int j)
    {
        for (int k = 0; k < min(land.size() - i, land[0].size() - j); k++)
        {
            if (land[i + k][j + k] == -1)
                return;
            if (land[i + k][j + k] == 0)
            {
                ans.push_back({i, j, i+k, j+k});
            }
        }
    }
};