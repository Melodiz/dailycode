class Solution
{
public:
    string replaceWords(vector<string>& dictionary, string sentence)
    {
        unordered_set<string> dict(dictionary.begin(), dictionary.end());
        string ans = "";
        istringstream iss(sentence);
        string word;
        while (iss >> word)
        {
            string prefix = "";
            for (int i = 0; i < word.size(); i++)
            {
                prefix += word[i];
                if (dict.find(prefix)!= dict.end())
                {
                    break;
                }
            }
            ans += prefix + " ";
        }
        return ans.substr(0, ans.size() - 1);

    }
};