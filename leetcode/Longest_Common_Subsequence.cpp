#include "iostream"
#include <string>
using namespace std;
class Solution
{
public:
    int longestCommonSubsequence(string text1, string text2)
    {
        int len_a = text1.size(), len_b = text2.size();
        int dp[len_a + 1][len_b + 1];

        memset(dp, 0, sizeof dp);

        for (int i = 1; i <= len_a; ++i)
        {
            for (int j = 1; j <= len_b; ++j)
            {
                if (text1[i - 1] == text2[j - 1])
                {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
                else
                {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[len_a][len_b];
    }
};