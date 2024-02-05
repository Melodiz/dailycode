#include "iostream"
#include <map>
#include <string>

class Solution
{
public:
    int firstUniqChar(string s)
    {
        map<char, int> dp;
        for (size_t i = 0; i < 26; i++)
        {
            dp[char(97 + i)] = -1;
        }

        for (size_t i = 0; i < s.size(); i++)
        {
            if (dp[s[i]] == -1)
            {
                dp[s[i]] = i;
            }
            else
            {
                dp[s[i]] = -2;
            }
        }
        int ans = pow(10, 6);

        for (size_t i = 97; i < 123; i++)
        {
            if (dp[char(i)] > -1)
            {
                ans = std::min(ans, dp[char(i)]);
            }
        }
        if (ans < pow(10, 6))
        {
            return ans;
        }
        return -1;
    }
};