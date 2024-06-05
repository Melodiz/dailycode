class Solution
{
public:
    vector<string> commonChars(vector<string>& words)
    {
        int n = words.size();
        // add all lowercase english letters to the map
        unordered_map<char, vector<int>> m;
        for (char c = 'a'; c <= 'z'; ++c)
        {
            m[c] = vector<int>(n, 0);
        }
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < words[i].size(); ++j)
            {
                m[words[i][j]][i]++;
            }
        }
        vector<string> res;
        {
            for (char c = 'a'; c <= 'z'; ++c)
            {
                // if all value of m[c] is true, then add c to res
                int min_freq = INT_MAX;
                for (int i = 0; i < n; ++i) {min_freq = min(min_freq, m[c][i]);}
                for (int i = 0; i < min_freq; ++i)
                {
                    res.push_back(string(1, c));
                }
            }
        }
        return res;
    }
};