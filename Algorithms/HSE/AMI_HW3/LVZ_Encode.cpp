#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>

std::vector<int> LVZ_encode(std::string message)
{
    // return the ecoded message as a vector of integers (with a ten-base representation)
    // add ascii values to the hesh table
        std::unordered_map<std::string, int> dictionary;
        for (int i = 0; i < 128; i++) {
            dictionary[std::string(1, char(i))] = i;
        }
    
        std::string current;
        std::vector<int> encoded_message;
        int dict_size = 128;
    
        for (char c : message) {
            std::string next = current + c;
            if (dictionary.find(next) != dictionary.end()) {
                current = next;
            } else {
                encoded_message.push_back(dictionary[current]);
                dictionary[next] = dict_size++;
                current = std::string(1, c);
            }
        }
    
        if (!current.empty()) {
            encoded_message.push_back(dictionary[current]);
        }
    
        return encoded_message;
    }

int main()
{
    std::string message;
    std::getline(std::cin, message);

    std::vector<int> encoded_message = LVZ_encode(message);
    std::cout << encoded_message.size() << std::endl;

    for (int num : encoded_message) {
        std::cout << num << " ";
    }

    std::cout << std::endl;

    return 0;
}