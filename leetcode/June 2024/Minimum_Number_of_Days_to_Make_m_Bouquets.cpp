class Solution
{
public:
    int minDays(vector<int>& bloomDay, int m, int k)
    {
        if (bloomDay.size() < (long)m * k) return -1;
        int l = 0;
        int r = *max_element(bloomDay.begin(), bloomDay.end());
        while (l < r)
        {
            int mid = l + (r - l) / 2;
            if (check(bloomDay, m, k, mid))
            {
                r = mid;
            }
            else
            {
                l = mid + 1;
            }
        }
        return l;
    }

    bool check(vector<int>& bloomDay, int m, int k, int day)
    {
        int count = 0;
        for (int i = 0; i < bloomDay.size(); i++)
        {
            if (bloomDay[i] <= day)
            {
                count++;
                if (count == k)
                {
                    count = 0;
                    m--;
                    if (m == 0) return true;
                }
            }
            else
            {
                count = 0;
            }
        }
        return false;
    }
};
