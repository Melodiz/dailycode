#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

std::string LZWDecompress(const std::vector<int>& compressed) {
    // Initialize the dictionary with ASCII characters
    std::unordered_map<int, std::string> dictionary;
    for (int i = 0; i < 128; ++i) {
        dictionary[i] = std::string(1, char(i));
    }

    std::string w(1, char(compressed[0]));
    std::string result = w;
    int dictSize = 128;

    for (size_t i = 1; i < compressed.size(); ++i) {
        int k = compressed[i];
        std::string entry;

        if (dictionary.find(k) != dictionary.end()) {
            entry = dictionary[k];
        } else if (k == dictSize) {
            entry = w + w[0];
        } else {
            throw std::runtime_error("Bad compressed k");
        }

        result += entry;

        // Add w+entry[0] to the dictionary
        dictionary[dictSize++] = w + entry[0];

        w = entry;
    }

    return result;
}

int main() {
    // Example compressed data
    int n;
    std::cin >> n;
    std::vector<int> compressed;
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        compressed.push_back(num);
    }

    try {
        std::string decompressed = LZWDecompress(compressed);
        std::cout << decompressed << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error during decompression: " << e.what() << std::endl;
    }

    return 0;
}