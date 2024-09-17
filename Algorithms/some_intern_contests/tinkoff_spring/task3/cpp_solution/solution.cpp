#include <iostream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>

std::string solution(const std::string& data_string, const std::unordered_set<char>& alphabet_set, int max_length) {
    std::unordered_set<std::string> substrings;
    int max_left = -1;
    int n = data_string.size();
    
    for (int left = 0; left < n; ++left) {
        std::unordered_map<char, int> char_count;
        int unique_chars = 0;
        for (int right = left; right < std::min(left + max_length, n); ++right) {
            char char_ = data_string[right];
            if (alphabet_set.find(char_) == alphabet_set.end()) {
                break;
            }
            if (char_count.find(char_) == char_count.end()) {
                char_count[char_] = 0;
                unique_chars++;
            }
            char_count[char_]++;
            std::string sub_string = data_string.substr(left, right - left + 1);
            if (unique_chars == alphabet_set.size()) {
                if (left > max_left) {
                    substrings = {sub_string};
                    max_left = left;
                } else if (left == max_left) {
                    substrings.insert(sub_string);
                }
            }
        }
    }
    
    if (substrings.empty()) {
        return "-1";
    }
    return *std::max_element(substrings.begin(), substrings.end(), [](const std::string& a, const std::string& b) {
        return a.size() < b.size();
    });
}

int main() {
    std::string data_string;
    std::cin >> data_string;
    std::string alphabet_input;
    std::cin >> alphabet_input;
    std::unordered_set<char> alphabet_set(alphabet_input.begin(), alphabet_input.end());
    int max_length;
    std::cin >> max_length;
    std::cout << solution(data_string, alphabet_set, max_length) << std::endl;
    return 0;
}