class Solution
{
public:
    int islandPerimeter(vector<vector<int>>& grid)
    {
        int ans = 0;
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j] == 1)
                {
                    ans += countNeighbors(grid, i, j);
                }
            }
        }
        return ans;
    }
    int countNeighbors(vector<vector<int>>& grid, int r, int c)
    {
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == 0)
        {
            return 1;
        }
        if (grid[r][c] == -1)
        {
            return 0;
        }
        grid[r][c] = -1;

        return (countNeighbors(grid, r + 1, c) +
                countNeighbors(grid, r - 1, c) +
                countNeighbors(grid, r, c + 1) +
                countNeighbors(grid, r, c - 1));
    }
};
