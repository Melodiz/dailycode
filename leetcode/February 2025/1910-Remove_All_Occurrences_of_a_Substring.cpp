#include <string>
#include <vector>

class Solution {
public:
    string removeOccurrences(string s, string part) {
        vector<char> result_stack;
        int target_length = part.length();
        char target_end_char = part.back();

        for (char current_char : s) {
            result_stack.push_back(current_char);

            if (current_char == target_end_char && result_stack.size() >= target_length) {
                string last_chars(result_stack.end() - target_length, result_stack.end());
                if (last_chars == part) {
                    result_stack.erase(result_stack.end() - target_length, result_stack.end());
                }
            }
        }

        return string(result_stack.begin(), result_stack.end());
    }
};