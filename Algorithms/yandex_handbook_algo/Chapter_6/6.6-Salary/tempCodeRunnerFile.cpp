#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

// Custom comparator function to sort numbers
bool compare(const std::string& a, const std::string& b)
{
    return std::stol(a + b) > std::stol(b + a);
}

std::string largestNumber(std::vector<int>& nums)
{
    // Convert all integers to strings
    std::vector<std::string> numStrs;
    for (int num: nums)
    {
        numStrs.push_back(std::to_string(num));
    }

    // Sort the numbers using the custom comparator
    std::sort(numStrs.begin(), numStrs.end(), compare);

    // Edge case: if the largest number is "0", the result should be "0"
    if (numStrs[0] == "0")
    {
        return "0";
    }

    // Concatenate the sorted numbers to form the largest number
    std::string result;
    for (const std::string& numStr: numStrs)
    {
        result += numStr;
    }

    return result;
}

int main()
{
    int n;
    std::cin >> n;
    std::vector<int> nums(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> nums[i];
    }

    std::string result = largestNumber(nums);
    std::cout << result << std::endl;

    return 0;
}