class Solution
{
public:
    // implement a function that returns the minimum number of operations needed to make
    // xor of all the elements equal to k
    int minOperations(vector<int>& nums, int k)
    {
        int res = nums[0];
        for (size_t i = 1; i < nums.size(); i++)
        {
            res = res ^ nums[i];
        }
        res = res ^ k;
        return countBits(res);

    }
    int countBits(int num)
    {
        // return the number of uniry bits in the binary representation of the given number
        int res = 0;
        while (num)
        {
            res += num & 1;
            num >>= 1;
        }
        return res;
    }
};