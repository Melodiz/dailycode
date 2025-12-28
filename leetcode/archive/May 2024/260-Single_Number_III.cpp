/*
Given an integer array nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that appear only once. 
You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
*/

class Solution
{
public:
    vector<int> singleNumber(vector<int>& nums)
    {
        int x = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            x = x ^ nums[i];
        }
        int mask = 1;
        while ((x & mask) == 0)
        {
            mask = mask << 1;
        }
        int a = 0;
        int b = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if ((nums[i] & mask) == 0)
            {
                a = a ^ nums[i];
            }
            else
            {
                b = b ^ nums[i];
            }
        }
        return {a, b};
    }
};