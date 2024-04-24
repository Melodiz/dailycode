class Solution
{
public:
    int tribonacci(int n)
    {
        if (n < 1 )
            return 0;
        if (n < 3)
            return 1;
        return rec(n-3, 1, 1, 0);
    }
    int rec(int n, int cur, int prev, int last)
    {
        if (n == 0)
            return cur+prev+last;
        return rec(n-1, cur+prev+last, cur, prev);
    }
};