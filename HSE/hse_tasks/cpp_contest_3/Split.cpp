#include "iostream"
#include <vector>
#include <string>

std::vector<std::string> split(const std::string &str, char delimiter);

std::vector<std::string> split(const std::string &str, char delimiter)
{
    std::vector<std::string> ans;
    std::string block = "";

    for (size_t i = 0; i < str.size(); i++)
    {
        if (str[i] == delimiter)
        {
            ans.push_back(block);
            block = "";
        }
        else
        {
            block += str[i];
        }
    }
    ans.push_back(block);

    return ans;
}

// int main()
// {
//     std::string input;
//     char sep;

//     std::cin >> input;
//     std::cin >> sep;

//     std::vector<std::string> ans = split(input, sep);

//     for (size_t i = 0; i < ans.size(); i++)
//     {
//         std::cout << ans[i];
//     }
//     std::cout << std::endl;

//     return 0;
// }
