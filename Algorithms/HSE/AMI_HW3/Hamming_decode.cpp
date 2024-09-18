#include <iostream>
#include <vector>
#include <cmath>
#include <string>

std::string decode_hamming_code(std::string hamming_code) {
    int n = hamming_code.length();
    int r = 0;

    // Calculate the number of parity bits
    while ((1 << r) < (n + 1)) {
        r++;
    }

    // Detect error position
    int error_pos = 0;
    for (int i = 0; i < r; i++) {
        int parity_pos = 1 << i;
        int parity = 0;
        for (int j = 1; j <= n; j++) {
            if (j & parity_pos) {
                parity ^= hamming_code[j - 1] - '0';
            }
        }
        if (parity != 0) {
            error_pos += parity_pos;
        }
    }

    // Correct the error if there is one
    if (error_pos != 0) {
        hamming_code[error_pos - 1] = (hamming_code[error_pos - 1] == '0') ? '1' : '0';
    }

    // Extract the original data
    std::string original_data;
    int j = 0;
    for (int i = 1; i <= n; i++) {
        if (i != (1 << j)) {
            original_data += hamming_code[i - 1];
        } else {
            j++;
        }
    }

    return original_data;
}

int main() {
    std::string hamming_code;
    std::cin >> hamming_code;
    std::string original_data = decode_hamming_code(hamming_code);
    std::cout << original_data << std::endl;
    return 0;
}