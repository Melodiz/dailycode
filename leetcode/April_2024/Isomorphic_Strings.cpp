class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> data;
        set<char> used;
        for (size_t i = 0; i < s.size(); i++)
        {  
            if (not data[s[i]])
            {
                if (used.contains(t[i]))
                    return false;
                data[s[i]] = t[i];
                used.insert(t[i]);
            }
            else if (data[s[i]] != t[i])
                return false;
            
        }
        return true;
        
    }
};