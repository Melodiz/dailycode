class Solution
{
public:
    int nthUglyNumber(int n)
    {
        vector<int> UglyNumber{1};
        int l1 = 0, l2 = 0, l3 = 0;
        while (UglyNumber.size() < n)
        {
            int a = UglyNumber[l1] * 2;
            int b = UglyNumber[l2] * 3;
            int c = UglyNumber[l3] * 5;
            int nextUgly = min({a, b, c});
            UglyNumber.push_back(nextUgly);
            if (nextUgly == a) l1++;
            if (nextUgly == b) l2++;
            if (nextUgly == c) l3++;
        }
        return UglyNumber.back();
    }
};