class Solution
{
public:
    vector<string> removeSubfolders(vector<string>& folder)
    {
        sort(folder.begin(), folder.end());
        vector<string> res;
        string prefix = "";
        for (const auto& f : folder)
        {
            if (f.find(prefix) != 0)
            {
                prefix = f;
                res.push_back(f);
            }
        }
        return res;
    }
};