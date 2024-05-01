class Solution
{
public:
    string reversePrefix(string word, char ch)
    {
        string prefix = word.substr(0, word.find(ch) + 1);
        // reverse the prefix
        reverse(prefix.begin(), prefix.end());
        return prefix + word.substr(word.find(ch) + 1);
    }
};