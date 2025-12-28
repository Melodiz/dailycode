class Solution
{
public:
    bool areAlmostEqual(string s1, string s2)
    {
        char m1, m2;
        int diff = 0;
        for (int i = 0; i < s1.size(); i++)
        {
            if (s1[i] != s2[i])
            {
                if (diff > 1)
                {
                    return false;
                }
                if (diff == 1)
                {
                    if (s1[i] == m2 && s2[i] == m1)
                    {
                        diff++;
                    }
                    else
                    {
                        return false;
                    }
                }
                if (diff == 0)
                {
                    m1 = s1[i];
                    m2 = s2[i];
                    diff++;
                }
            }
        }
        if (diff == 1)
        {
            return false;
        }
        return true;
    }
};