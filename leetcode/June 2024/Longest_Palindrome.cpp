class Solution
{
public:
    int longestPalindrome(string s)
    {
        int oddCount = 0;
        unordered_map<char, int> ump;
        for (char ch: s)
        {
            ump[ch]++;
        }
        for (int i = 0; i < ump.size(); i++)
        {
            if (ump[i] % 2 == 1) { oddCount++;}
        }
        if (oddCount > 1)
            return s.length() - oddCount + 1;
        return s.length();
    }
};