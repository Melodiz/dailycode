#include "iostream"
#include <string>

std::string common_suffix(const std::string &a, const std::string &b);

std::string common_suffix(const std::string &a, const std::string &b)
{
    std::string ans = "";

    for (size_t i = 0; i < std::min(a.size(), b.size()); i++)
    {
        if (a[i]==b[i])
        {
            ans+=a[i];
        }
        return ans;
    }
    reverse(suf.begin(), suf.end());
    return ans;
}