#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

const int ALPHABET_SIZE = 26;

class TrieNode {
public:
    TrieNode* children[ALPHABET_SIZE];
    bool is_end;
    int count;

    TrieNode() : is_end(false), count(0) {
        for (int i = 0; i < ALPHABET_SIZE; i++) {
            children[i] = nullptr;
        }
    }
};

class Trie {
private:
    TrieNode* root;

    std::string find_kth_helper(TrieNode* node, int& k) {
        if (k <= 0 || !node) {
            return "";
        }

        for (int i = 0; i < ALPHABET_SIZE; i++) {
            TrieNode* child = node->children[i];
            if (child && k <= child->count) {
                if (child->is_end && k == 1) {
                    return std::string(1, 'a' + i);
                }
                k -= (child->is_end ? 1 : 0);
                return std::string(1, 'a' + i) + find_kth_helper(child, k);
            }
            if (child) {
                k -= child->count;
            }
        }

        return "";
    }

public:
    Trie() : root(new TrieNode()) {}

    void insert(const std::string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->children[index]) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
            node->count++;
        }
        node->is_end = true;
    }

    std::string find_kth(int k) {
        return find_kth_helper(root, k);
    }
};

int main() {
    int n;
    std::cin >> n;
    Trie trie;

    for (int i = 0; i < n; i++) {
        std::string command;
        std::cin >> command;
        if (isdigit(command[0])) {
            int k = std::stoi(command);
            std::cout << trie.find_kth(k) << std::endl;
        } else {
            trie.insert(command);
        }
    }

    return 0;
}