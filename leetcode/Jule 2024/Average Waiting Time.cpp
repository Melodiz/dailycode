class Solution
{
public:
    double averageWaitingTime(vector<vector<int>>& customers)
    {
        long long waitingTime = customers[0][1];
        int n = customers.size();
        int curTime = customers[0][0];
        int queTime = curTime + customers[0][1];
        for (size_t i = 1; i < n; ++i)
        {
            if (customers[i][0] >= queTime)
            {
                waitingTime += customers[i][1];
                queTime = customers[i][0] + customers[i][1];
            }
            else
            {
                queTime += customers[i][1];
                waitingTime += queTime - customers[i][0];
            }
        }
        return static_cast<double>(waitingTime) / n;
    }
};