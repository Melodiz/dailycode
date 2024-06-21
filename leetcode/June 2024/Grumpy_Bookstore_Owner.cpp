class Solution
{
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes)
    {
        int n = customers.size();
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            if (i < minutes || !grumpy[i])
                sum += customers[i];
        }
        int ans = sum; // use from 0 to minutes-1 
        // now shift to the right, and update the sum
        for (int i = minutes; i < n; i++)
        {
            if (grumpy[i]) sum += customers[i];
            if (grumpy[i - minutes]) sum -= customers[i - minutes];
            ans = max(ans, sum); // update the answer
        }
        return ans;
    }
};