class Solution
{
public:
    int minBitFlips(int start, int goal)
    {
        int flips = 0;
        int xorResult = start ^ goal;
        while (xorResult)
        {
            flips += xorResult & 1;
            xorResult >>= 1;
        }
        return flips;
    }
};