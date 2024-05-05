class Solution
{
public:
    int equalPairs(vector<vector<int>>& grid)
    {
        // return amout of equal pairs of rows and columns
        int n = grid[0].size();
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                if (isEqual(grid, i, j, n))
                    ans++;
            }
        }
        return ans;
    }
    
    bool isEqual(vector<vector<int>>& grid, int i, int j, int n)
    {
        // return true if row i and column j are equal
        // else return false
        for (int k = 0; k < n; k++)
        {
            if (grid[i][k]!= grid[k][j])
                return false;
        }
        return true;
    }
};