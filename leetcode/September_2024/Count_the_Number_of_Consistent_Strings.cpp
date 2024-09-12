class Solution
{
public:
    int countConsistentStrings(string allowed, vector<string>& words)
    {
        // convert the allowed string to unordered_set for faster lookup
        unordered_set<char> allowedSet(allowed.begin(), allowed.end());

        // iterate over each word in the vector and check if it's consistent with the allowed string
        int consistentCount = 0;
        for (string &word : words)
        {
            bool isConsistent = true;
            for (char c : word)
            {
                if (allowedSet.find(c) == allowedSet.end())
                {
                    isConsistent = false;
                    break;
                }
            }
            if (isConsistent)
            {
                consistentCount++;
            }
        }

        return consistentCount;
    }
};