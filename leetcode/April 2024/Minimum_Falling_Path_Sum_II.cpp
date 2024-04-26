class Solution
{
public:
    int minFallingPathSum(vector<vector<int>>& grid)
    {
        int n = grid.size();

        for (int i = 1; i < n; i++)
        {
            vector<int> row = grid[i - 1];
            nth_element(row.begin(), row.begin() + 1, row.end());
            for (int j = 0; j < n; j++)
            {
                if (grid[i - 1][j] == row[0])
                    grid[i][j] += row[1];
                else
                    grid[i][j] += row[0];
            }
        }

        return *min_element(grid[n - 1].begin(), grid[n - 1].end());
    }
};