class Solution
{
public:
    int uniquePaths(int m, int n)
    {
        // create a 2D array with m rows and n columns and fill it with 0
        int MOD = 2*1e9
        vector<vector<int>> dp(m, vector<int>(n, 0));
        // fill the first row and first column with 1
        for (int i = 0; i < m; i++)
        {
            dp[i][0] = 1;
        }
        for (int i = 0; i < n; i++)
        {
            dp[0][i] = 1;
        }
        // fill the rest of the array
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
            }
        }
        return dp[m-1][n-1];
    }
};