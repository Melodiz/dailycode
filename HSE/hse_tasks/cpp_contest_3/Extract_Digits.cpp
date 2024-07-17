#include <iostream>
#include <string>
#include <fstream>
#include <sstream> 

std::string ExtractDigits(const std::string &s);

std::string ExtractDigits(const std::string &s)
{
    std::string ans = "";
    for (size_t i = 0; i < s.length(); i++)
    {
        if (int(s[i]) > 47 && int(s[i]) < 58)
        {
            ans += s[i];
        }
    }
    return ans;
}