class Solution
{
public:
    int largestCombination(vector<int>& candidates)
    {
        sort(candidates.rbegin(), candidates.rend());
        int result = 0;
        for (int i = 0; i < candidates.size() && candidates[i] <= result; i++)
            result += candidates[i];
        return result;
    }
};