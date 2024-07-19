#include <iostream>
#include <vector>

bool canWin(int n, int m)
{
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));

    for (int i = 0; i <= n; ++i)
    {
        for (int j = 0; j <= m; ++j)
        {
            if (i == 0 && j == 0)
            {
                dp[i][j] = 0;// No stones left, losing position
            }
            else
            {
                bool win = false;
                if (i > 0 && !dp[i - 1][j]) dp[i][j] = 1;
                else if (j > 0 && !dp[i][j - 1])
                    dp[i][j] = 1;
                else if (i > 1 && !dp[i - 2][j])
                    dp[i][j] = 1;
                else if (j > 1 && !dp[i][j - 2])
                    dp[i][j] = 1;
                else if (i > 1 && j > 0 && !dp[i - 2][j - 1])
                    dp[i][j] = 1;
                else if (i > 0 && j > 1 && !dp[i - 1][j - 2])
                    dp[i][j] = 1;
            }
        }
    }
    return dp[n][m];
}

int main()
{
    int n, m;
    std::cin >> n >> m;
    if (canWin(n, m))
    {
        std::cout << "Win\n";
    }
    else
    {
        std::cout << "Loose\n";
    }
    return 0;
}