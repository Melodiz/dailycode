#include <iostream>
#include <vector>
#include <cmath>
#include <string>

std::string calculate_parity_bits(std::string data) {
    int n = data.length();
    int r = 0;

    // Calculate the number of parity bits needed
    while ((1 << r) < (n + r + 1)) {
        r++;
    }

    // Initialize the array with parity bits set to 0
    std::vector<char> hamming_code(n + r, '0');
    int j = 0;

    // Place the data bits in the correct positions
    for (int i = 1; i <= hamming_code.size(); i++) {
        if (i == (1 << j)) {
            j++;
        } else {
            hamming_code[i - 1] = data[0];
            data = data.substr(1);
        }
    }

    // Calculate the parity bits
    for (int i = 0; i < r; i++) {
        int parity_pos = 1 << i;
        int parity = 0;
        for (int j = 1; j <= hamming_code.size(); j++) {
            if (j & parity_pos) {
                parity ^= hamming_code[j - 1] - '0';
            }
        }
        hamming_code[parity_pos - 1] = parity + '0';
    }

    return std::string(hamming_code.begin(), hamming_code.end());
}

int main() {
    std::string data;
    std::cin >> data;
    std::string hamming_code = calculate_parity_bits(data);
    std::cout << hamming_code << std::endl;
    return 0;
}