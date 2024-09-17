#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cassert>
#include <chrono>
#include <iomanip>
#include <random>

std::string solver(const std::string& data_string, const std::unordered_set<char>& alphabet_set, int max_length) {
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
                    substrings.clear();
                    substrings.insert(sub_string);
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

void save_to_file(const std::string& filename, const std::vector<std::tuple<std::string, std::set<char>, int>>& test_cases)
{
    std::ofstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return;
    }

    for (const auto& [data, alphabet, max_len] : test_cases) {
        file << data << " " << alphabet.size() << " ";
        for (char c : alphabet) {
            file << c;
        }
        file << " " << max_len << std::endl;
    }
    file.close();
}

void generate_random_test_cases(int num_test_cases = 30, int n = 200000) {
    std::vector<std::tuple<std::string, std::set<char>, int>> test_cases;
    std::vector<std::string> expected_outputs;
    std::string full_alphabet = "abcdefghijklmnopqrstuvwxyz";
    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist1(1, 26);
    std::uniform_int_distribution<int> dist2(1, n);
    std::uniform_int_distribution<int> dist3(0, 25);

    for (int i = 0; i < num_test_cases; ++i) {
        std::set<char> allowed_alphabet;
        int alphabet_size = dist1(rng);
        while (allowed_alphabet.size() < alphabet_size) {
            allowed_alphabet.insert(full_alphabet[dist3(rng)]);
        }
        std::set<char> test_case_alphabet = allowed_alphabet;
        while (test_case_alphabet.size() < dist1(rng)) {
            test_case_alphabet.insert(full_alphabet[dist3(rng)]);
        }
        int max_length = dist2(rng);
        std::string data_string;
        for (int j = 0; j < n; ++j) {
            data_string += full_alphabet[dist3(rng)];
        }
        test_cases.emplace_back(data_string, test_case_alphabet, max_length);
        std::unordered_set<char> test_case_alphabet_unordered(test_case_alphabet.begin(), test_case_alphabet.end());
        expected_outputs.push_back(solver(data_string, test_case_alphabet_unordered, max_length));
    }

    save_to_file("large_tests.txt", test_cases);
    std::cout << "Generated " << num_test_cases << " random test cases." << std::endl;
}

int main() {
    generate_random_test_cases();
    return 0;
}