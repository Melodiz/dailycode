class Solution
{
public:
    int numTilings(int n)
    {
        return rec(n);
    }
    int rec(int n)
    {
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (n == 3) return 5;
        if (n == 4) return 11;
        return (rec(n - 1) + rec(n - 2) + rec(n - 3) + rec(n - 4)) % (pow(10, 9) + 7);
    }
};