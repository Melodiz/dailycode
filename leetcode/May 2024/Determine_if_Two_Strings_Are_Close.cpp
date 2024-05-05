class Solution
{
public:
    bool closeStrings(string word1, string word2)
    {
        // constuct a map for each word to store the count of each character

        unordered_map<char, int> m1, m2;
        for (char c: word1)
            m1[c]++;
        for (char c: word2)
            m2[c]++;

        // check if the two words have the same characters
        if (m1.size() != m2.size()) return false;
        for (auto p: m1)
        {
            if (m2.find(p.first) == m2.end()) return false; // if not found, return false
        }

        // check if the two words have the same count of each character
        std::vector<int> v1, v2;
        for (auto p: m1)
        {
            v1.push_back(p.second);
            v2.push_back(m2[p.first]);
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        if (v1!= v2) return false;

        return true;
    }
};