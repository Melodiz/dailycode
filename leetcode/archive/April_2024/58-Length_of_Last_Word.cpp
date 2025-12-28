class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int n = s.size();
        int start;

        for (int i = n - 1; i >= 0; i--)
        {
            if (s[i] != ' ')
            {
                start = i;
                break;
            }
        }
        int count = 0;
        for (int i = start; i >= 0; i--)
        {
            if (s[i] == ' ')
                break;

            count++;
        }

        return count;
    }
};