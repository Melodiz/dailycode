class Solution
{
public:
    string removeStars(string s)
    {
        std::vector<char> st;
        for (int i = 0; i < s.length(); ++i)
        {
            if (s[i] == '*')
                st.pop_back();
            else
                st.push_back(s[i]);
        }
        std::string ans(st.begin(), st.end());
        return ans;
    }
};