class Solution
{
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target)
    {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> combination;
        combinationSum2Helper(candidates, target, 0, combination, result);
        return result;
    }

    void combinationSum2Helper(vector<int>& candidates, int target, int start, vector<int>& combination, vector<vector<int>>& result)
    {
        if (target == 0)
        {
            result.push_back(combination);
            return;
        }

        for (int i = start; i < candidates.size() && target >= candidates[i]; ++i)
        {
            if (i > start && candidates[i] == candidates[i - 1])
                continue;

            combination.push_back(candidates[i]);
            combinationSum2Helper(candidates, target - candidates[i], i + 1, combination, result);
            combination.pop_back();
        }
        return;
    }
};