#include <algorithm>
#include <cassert>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

std::string solution(const std::string& data_string, const std::unordered_set<char>& alphabet_set, int max_length)
{
    std::unordered_set<std::string> substrings;
    int max_left = -1;
    int n = data_string.size();

    for (int left = 0; left < n; ++left)
    {
        std::unordered_map<char, int> char_count;
        int unique_chars = 0;
        for (int right = left; right < std::min(left + max_length, n); ++right)
        {
            char char_ = data_string[right];
            if (alphabet_set.find(char_) == alphabet_set.end())
            {
                break;
            }
            if (char_count.find(char_) == char_count.end())
            {
                char_count[char_] = 0;
                unique_chars++;
            }
            char_count[char_]++;
            std::string sub_string = data_string.substr(left, right - left + 1);
            if (unique_chars == alphabet_set.size())
            {
                if (left > max_left)
                {
                    substrings.clear();
                    substrings.insert(sub_string);
                    max_left = left;
                }
                else if (left == max_left)
                {
                    substrings.insert(sub_string);
                }
            }
        }
    }

    if (substrings.empty())
    {
        return "-1";
    }
    return *std::max_element(substrings.begin(), substrings.end(), [](const std::string& a, const std::string& b) {
        return a.size() < b.size();
    });
}

std::pair<std::vector<std::tuple<std::string, std::set<char>, int>>, std::vector<std::string>> read_data(const std::string& file_path = "task3/test_cases.txt")
{
    std::vector<std::tuple<std::string, std::set<char>, int>> cases;
    std::vector<std::string> expected_outputs;
    std::ifstream file(file_path);
    std::string line;
    std::vector<std::string> arr;

    while (std::getline(file, line))
    {
        arr.push_back(line);
    }

    for (size_t i = 0; i < arr.size(); i += 4)
    {
        std::string data_string = arr[i];
        std::set<char> alphabet_set(arr[i + 1].begin(), arr[i + 1].end());
        int max_length = std::stoi(arr[i + 2]);
        cases.emplace_back(data_string, alphabet_set, max_length);
        expected_outputs.push_back(arr[i + 3]);
    }

    return {cases, expected_outputs};
}

void run_tests()
{
    auto [cases, expected_outputs] = read_data();
    for (size_t i = 0; i < cases.size(); ++i)
    {
        const auto& [data_string, alphabet_set, max_length] = cases[i];
        std::unordered_set<char> alphabet_set_unordered(alphabet_set.begin(), alphabet_set.end());
        std::string output = solution(data_string, alphabet_set_unordered, max_length);
        assert(expected_outputs[i] == output && "Test case failed");
    }
    std::cout << "Tinkoff test cases passed." << std::endl;

    auto [random_cases1, random_expected_outputs1] = read_data("random_tests.txt");
    auto starttime1 = std::chrono::high_resolution_clock::now();
    for (size_t i = 0; i < random_cases1.size(); ++i)
    {
        const auto& [data_string, alphabet_set, max_length] = random_cases1[i];
        std::unordered_set<char> alphabet_set_unordered(alphabet_set.begin(), alphabet_set.end());
        std::string output = solution(data_string, alphabet_set_unordered, max_length);
        assert(random_expected_outputs1[i] == output && "Random test case failed");
    }
    auto endtime1 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed1 = endtime1 - starttime1;
    std::cout << "Random test cases passed in " << std::fixed << std::setprecision(4) << elapsed1.count() << " seconds." << std::endl;

    auto [random_cases2, random_expected_outputs2] = read_data("large_tests.txt");
    auto starttime2 = std::chrono::high_resolution_clock::now();
    for (size_t i = 0; i < random_cases2.size(); ++i)
    {
        const auto& [data_string, alphabet_set, max_length] = random_cases2[i];
        std::unordered_set<char> alphabet_set_unordered(alphabet_set.begin(), alphabet_set.end());
        std::string output = solution(data_string, alphabet_set_unordered, max_length);
        assert(random_expected_outputs2[i] == output && "Large test case failed");
    }
    auto endtime2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed2 = endtime2 - starttime2;
    std::cout << "Large test cases passed in " << std::fixed << std::setprecision(4) << elapsed2.count() << " seconds." << std::endl;
}

int main()
{
    run_tests();
    return 0;
}