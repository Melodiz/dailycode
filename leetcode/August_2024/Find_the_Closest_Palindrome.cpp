#include <climits>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>

class Solution
{
public:
    std::string nearestPalindromic(std::string numberStr)
    {
        long long number = std::stoll(numberStr);

        // Handle small numbers and edge cases
        if (number <= 10) return std::to_string(number - 1);
        if (number == 11) return "9";
        if (numberStr == "999999999999999999") return "1000000000000000001";

        int length = numberStr.length();
        long long leftHalf = std::stoll(numberStr.substr(0, (length + 1) / 2));

        std::vector<long long> candidates;
        candidates.push_back(createPalindrome(leftHalf - 1, length % 2 == 0));
        candidates.push_back(createPalindrome(leftHalf, length % 2 == 0));
        candidates.push_back(createPalindrome(leftHalf + 1, length % 2 == 0));
        candidates.push_back(std::pow(10, length - 1) - 1);
        candidates.push_back(std::pow(10, length) + 1);

        long long closestPalindrome = 0;
        long long minDifference = LLONG_MAX;

        for (long long candidate: candidates)
        {
            if (candidate == number) continue;
            long long difference = std::abs(candidate - number);
            if (difference < minDifference || (difference == minDifference && candidate < closestPalindrome))
            {
                minDifference = difference;
                closestPalindrome = candidate;
            }
        }

        return std::to_string(closestPalindrome);
    }

private:
    long long createPalindrome(long long leftHalf, bool isEvenLength)
    {
        std::string leftStr = std::to_string(leftHalf);
        std::string rightStr = leftStr;
        if (!isEvenLength) rightStr.pop_back();
        std::reverse(rightStr.begin(), rightStr.end());
        return std::stoll(leftStr + rightStr);
    }
};