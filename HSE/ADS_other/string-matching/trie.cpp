#include <string>
#include <vector>
#include <map>
class TrieNode
{
public:
    bool endofWord;
    char value;
    std::map<char,TrieNode*> children;

    TrieNode()
    {
        value = char(0);
        endofWord = false;
        children = {};
    }
};

class Trie
{
private:
    TrieNode* root;

public:
    Trie() { root = new TrieNode(); }
    void insert(std::string& word)
    {
        TrieNode* node = root;
        for (char c : word)
        {
            break;
        }
    }
};