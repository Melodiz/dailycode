#include "iostream"
#include "string"
using namespace std;

class Solution
{
public:
    string helper(string s)
    {
        string ans = "";
        for (size_t i = 0; i < s.length(); i++)
        {
            if (abs(char(s[i]) - char(s[i + 1])) == 32)
                i++;
            else
                ans += s[i];
        }
        return ans;
    }
    string makeGood(string s)
    {
        while (s.length() > 1)
        {
            string n = helper(s);
            if (s != n)
                s = n;
            else
                return s;
        }
        return s;
    }
};

int main()
{
    string val = "leEeetcode";
    Solution test;
    cout << test.makeGood(val);
    // string ans = test.makeGood(val)

    return 0;
}