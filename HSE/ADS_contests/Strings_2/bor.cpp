#include <iostream>
#include <string>
#include <vector>

const int ALPHABET_SIZE = 26;

class TrieNode {
public:
    TrieNode* children[ALPHABET_SIZE];
    int value;

    TrieNode() : value(0) {
        for (int i = 0; i < ALPHABET_SIZE; i++) {
            children[i] = nullptr;
        }
    }
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() : root(new TrieNode()) {}

    int add(const std::string& variable, int delta) {
        TrieNode* node = root;
        for (char c : variable) {
            int index = c - 'a';
            if (!node->children[index]) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->value += delta;
        return node->value;
    }
};

int main() {
    Trie trie;
    std::string variable;
    int delta;

    while (std::cin >> variable >> delta) {
        std::cout << trie.add(variable, delta) << std::endl;
    }

    return 0;
}