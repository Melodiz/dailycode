class Solution
{
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid)
    {
        int n = grid.size();
        vector<vector<int>> res(n - 2, vector<int>(n - 2));
        for (int i = 0; i < n - 2; ++i)
        {
            for (int j = 0; j < n - 2; ++j)
            {
                res[i][j] = max(grid[i][j], max(grid[i][j + 1], max(grid[i][j + 2], max(grid[i + 1][j], max(grid[i + 1][j + 1], max(grid[i + 1][j + 2], max(grid[i + 2][j], max(grid[i + 2][j + 1], grid[i + 2][j + 2]))))))));
            }
        }
        return res;
    }
};