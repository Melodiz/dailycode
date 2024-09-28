class Solution
{
public:
    int maxVowels(string s, int k)
    {
        int res = 0, cur = 0;
        map<char, int> vowels = {{'a', 1}, {'e', 1}, {'i', 1}, {'o', 1}, {'u', 1}};

        for (int i = 0; i < s.length(); i++)
        {
            // Add the current character if it's a vowel
            cur += vowels[s[i]];

            // Once we've added the kth character, start subtracting the character that's leaving the window
            if (i >= k)
            {
                cur -= vowels[s[i - k]];
            }

            // Update the result with the maximum number of vowels seen so far
            res = max(res, cur);
        }
        return res;
    }
};