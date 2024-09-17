class Solution
{
public:
    vector<string> uncommonFromSentences(string s1, string s2)
    {
        unordered_map<string, int> wordCount;
        stringstream ss1(s1 + " " + s2);
        string word;

        while (ss1 >> word)
        {
            ++wordCount[word];
        }

        vector<string> result;
        for (const auto& pair : wordCount)
        {
            if (pair.second == 1)
            {
                result.push_back(pair.first);
            }
        }

        return result;
    }
};