class Solution
{
public:
    int maxDepth(string s)
    {
        int cur = 0;
        int ans = 0;

        for (size_t i = 0; i < s.length(); i++)
        {
            if (s[i] == '(')
                cur++;
            else if (s[i] == ')')
            {
                ans = max(cur, ans);
                cur--;
            }
        }
        return ans;
    }
};