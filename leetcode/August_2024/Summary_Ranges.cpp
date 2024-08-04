#include <vector>
#include <string>

class Solution
{
public:
    std::vector<std::string> summaryRanges(std::vector<int>& nums)
    {
        std::vector<std::string> result;
        if (nums.empty()) {
            return result;  // Return empty result if input is empty
        }

        int start = nums[0];  // Initialize start of the range
        int prev = nums[0];   // Initialize previous number

        for (int i = 1; i < nums.size(); ++i)
        {
            if (nums[i] == prev + 1) {
                // Continue the range
                prev = nums[i];
            } else {
                // End the current range and start a new one
                if (start == prev) {
                    result.push_back(std::to_string(start));
                } else {
                    result.push_back(std::to_string(start) + "->" + std::to_string(prev));
                }
                start = nums[i];
                prev = nums[i];
            }
        }

        // Add the last range
        if (start == prev) {
            result.push_back(std::to_string(start));
        } else {
            result.push_back(std::to_string(start) + "->" + std::to_string(prev));
        }

        return result;
    }
};