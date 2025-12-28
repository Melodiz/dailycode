class Solution
{
public:
    string makeFancyString(string s)
    {
        if (s.length() < 3)
        {
            return s;
        }
        
        string result = "";
        result += s[0];
        result += s[1];
        
        for (int i = 2; i < s.length(); i++)
        {
            char p1 = result[result.length() - 1];
            char p2 = result[result.length() - 2];
            
            if (!(s[i] == p1 && s[i] == p2))
            {
                result += s[i];
            }
        }
        
        return result;
    }
};