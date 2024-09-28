#include <string>
#include <vector>
#include <algorithm>

class Solution
{
public:
    int lengthOfLongestSubstring(std::string s)
    {
        int max_window = 0;
        int left = 0, right = 0;
        std::vector<int> char_index(128, -1); // Initialize with -1 to indicate that characters are not yet seen

        while (right < s.length())
        {
            if (char_index[s[right]] != -1) {
                // If the character is already in the window, move the left pointer
                left = std::max(left, char_index[s[right]] + 1);
            }
            // Update the last seen index of the character
            char_index[s[right]] = right;
            // Calculate the maximum window size
            max_window = std::max(max_window, right - left + 1);
            // Move the right pointer
            right++;
        }
        return max_window;
    }
};