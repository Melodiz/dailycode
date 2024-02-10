#include "iostream"
#include <vector>
#include <string>

std::string join(const std::vector<std::string>& tokens, char delimiter);


std::string join(const std::vector<std::string>& tokens, char delimiter)
{
    std::string ans = "";

    for (size_t i = 0; i < tokens.size(); i++)
    {
        ans += tokens[i] + delimiter;
    }
    ans.pop_back();
    return ans;
}


// int main()
// {
//     vector<string> data;
//     size_t n = 0;
//     char sep;
//     string input;

//     cin >> n;

//     for (size_t i = 0; i < n; i++)
//     {
//         cin >> input;
//         data.push_back(input);
//     }
//     cin >> sep;

//     cout << join(data, sep, n) << endl;
// }