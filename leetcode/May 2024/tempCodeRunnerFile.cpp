#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>

class Solution
{
public:
    std::string decodeString(std::string s)
    {
        std::string result = "";
        std::string val = "";
        std::string store = "";
        int i = 0;
        while (i < s.size())
        {
            while (s[i] != '[' && i < s.size())
            {
                val += s[i];
                i++;
            }
            i++;
            while (s[i] != ']' && i < s.size())
            {
                store += s[i];
                i++;
            }
            i++;
            std::cout << val << std::endl;
            for (int j = 0; j < stoi(val); j++) { result += store; }
            val = "";
            store = "";
        }
        return result;
    }
};

int main()
{
    Solution s;
    std::cout << s.decodeString("3[a]2[bc]") << std::endl;
    Solution s1;
    std::cout << s1.decodeString("3[a2[c]]") << std::endl;
    Solution s2;
    std::cout << s2.decodeString("2[abc]3[cd]ef") << std::endl;
    return 0;
}