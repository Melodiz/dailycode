#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cassert>
#include <random>

// Custom comparator function to sort numbers
bool compare(const std::string& a, const std::string& b)
{
    return a + b > b + a;
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

// Brute force solution to generate all permutations and find the largest number
std::string bruteForceLargestNumber(std::vector<int>& nums) {
    std::vector<std::string> numStrs;
    for (int num : nums) {
        numStrs.push_back(std::to_string(num));
    }
    std::sort(numStrs.begin(), numStrs.end());
    std::string maxNumber;
    do {
        std::string currentNumber;
        for (const std::string& numStr : numStrs) {
            currentNumber += numStr;
        }
        if (currentNumber > maxNumber) {
            maxNumber = currentNumber;
        }
    } while (std::next_permutation(numStrs.begin(), numStrs.end()));

    return maxNumber;
}

std::string printVector(const std::vector<int>& nums) {
    std::string result;
    for (int num : nums) {
        result += std::to_string(num) + " ";
    }
    return result.substr(0, result.size() - 1);
}

void testLargestNumber() {
    std::vector<std::vector<int>> testCases = {
        {3, 30, 34, 5, 9},
        {10, 2},
        {1},
        {10, 0},
        {999, 99, 9}
    };

    // Generate 100 random test cases
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distLen(2, 10);
    std::uniform_int_distribution<> distVal(0, 30);

    for (int i = 0; i < 100; ++i) {
        int len = distLen(gen);
        std::vector<int> randomTestCase(len);
        for (int& num : randomTestCase) {
            num = distVal(gen);
        }
        testCases.push_back(randomTestCase);
    }

    for (auto& testCase : testCases) {
        std::string expected = bruteForceLargestNumber(testCase);
        std::string result = largestNumber(testCase);
        std::cout << "Input: " << printVector(testCase) << ", Expected: " << expected << ", Result: " << result << std::endl;
        assert(result == expected && "Test case failed");
    }

    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    testLargestNumber();
    return 0;
}