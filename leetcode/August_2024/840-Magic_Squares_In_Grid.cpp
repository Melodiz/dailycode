class Solution
{
public:
    int numMagicSquaresInside(vector<vector<int>>& grid)
    {
        int ans = 0;
        int n = grid.size();
        int m = grid[0].size();
        for (int i = 1; i < n - 1; i++)
        {
            for (int j = 1; j < m - 1; j++)
            {
                if (check(grid, i, j))
                {
                    ans++;
                }
            }
        }
        return ans;
    }

private:
    bool check(vector<vector<int>>& grid, int x, int y)
    {
        // check that the 3x3 square with center at (x, y) is a magic square
        // magic square is a with all distinct digits from 1 to 9 and the sum of each row, column have the same sum

        // check the borders
        if (x < 1 || x > grid.size() - 2 || y < 1 || y > grid[0].size() - 2) { return false; }

        // check that numbers are distinct and between 1 and 9
        vector<int> count(10, 0);
        for (int i = x - 1; i <= x + 1; i++)
        {
            for (int j = y - 1; j <= y + 1; j++)
            {
                int num = grid[i][j];
                if (num < 1 || num > 9 || count[num] > 0) { return false; }
                count[num]++;
            }
        }

        // check the sums
        int s1 = grid[x - 1][y - 1] + grid[x - 1][y] + grid[x - 1][y + 1];
        int s2 = grid[x][y - 1] + grid[x][y] + grid[x][y + 1];
        int s3 = grid[x + 1][y - 1] + grid[x + 1][y] + grid[x + 1][y + 1];
        if (s1 != s2 || s2 != s3) { return false; }

        int s4 = grid[x - 1][y - 1] + grid[x][y - 1] + grid[x + 1][y - 1];
        int s5 = grid[x - 1][y] + grid[x][y] + grid[x + 1][y];
        int s6 = grid[x - 1][y + 1] + grid[x][y + 1] + grid[x + 1][y + 1];
        if (s1 != s4 || s4 != s5 || s5 != s6) { return false; }

        int s7 = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1];
        int s8 = grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1];
        if (s1 != s7 || s7 != s8) { return false; }

        return true;
    }
};