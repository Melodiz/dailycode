/*
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b
*/

class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < (1 << nums.size()); ++i) {
            int cur = 0;
            for (int j = 0; j < nums.size(); ++j) {
                if (i & (1 << j)) {
                    cur ^= nums[j];
                }
            }
            res += cur;
        }
        return res;
    }
};