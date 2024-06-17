class Solution
{
public:
    bool judgeSquareSum(int c)
    {
        int i = 0;
        int j = static_cast<int>(sqrt(c));
        while (i <= j)
        {
            long long sum = static_cast<long long>(i) * i + static_cast<long long>(j) * j;
            if (sum == c)
                return true;
            else if (sum < c)
                i++;
            else
                j--;
        }
        return false;
    }
};