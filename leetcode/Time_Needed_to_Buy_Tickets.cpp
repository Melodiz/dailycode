class Solution
{
public:
    int timeRequiredToBuy(vector<int>& tickets, int k)
    {
        int i = 0;
        int ans = 0;
        int n = tickets.size();
        while (tickets[k])
        {
            if (tickets[i%n])
            {
               tickets[i%n]--; 
               ans++;
            }
            i++;
        }
        return ans;
    }
};