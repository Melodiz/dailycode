class Solution
{
public:
    static vector<int> missingRolls(vector<int>& rolls, int mean, int n)
    {
        const int m = rolls.size(); // Number of rolls 
        const int sum_rolles = accumulate(rolls.begin(), rolls.end(), 0); // Sum of all rolls 
        const int total = (n + m) * mean, miss = total - sum_rolles; // Calculate the total sum and missing rolls 
        //    cout<<total<<", miss="<<miss<<endl;
        if (miss > 6 * n || miss < n) return {}; // If the missing rolls are out of range, return an empty vector
        auto [q, r] = div(miss, n); // Calculate the number of groups and remainder 
        vector<int> ans(n, q); // Fill the groups with the calculated number of rolls 
        fill(ans.begin(), ans.begin() + r, q + 1); // Fill the remainder with the next possible roll 
        return ans; 
    }
};

// for better performance
auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();