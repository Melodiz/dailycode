#include <iostream>
#include <string>
#include <algorithm>

std::string common_suffix(const std::string &a, const std::string &b);

std::string common_suffix(const std::string &a, const std::string &b)
{
    std::string ans = "";
    int lenA = a.length()-1;
    int lenB = b.length()-1;

    while (lenA>=0 && lenB>=0 && a[lenA] == b[lenB])
    {
        ans += a[lenA];
        lenA--;
        lenB--;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}
