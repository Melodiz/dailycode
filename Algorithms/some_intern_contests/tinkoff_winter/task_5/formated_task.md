You are given a rod with n segments, each separated by a notch. The length of the i-th segment is a_i. You can only cut the rod at the notches, and a piece is considered small if its length does not exceed s. Your goal is to minimize the number of cuts needed to ensure all pieces are small.

For a sub-rod defined by segments a_l, a_l+1, ..., a_r, determine the minimum number of cuts required so that each piece is small. Denote this value as f(l, r).

Calculate the sum of f(l, r) for all possible sub-rods, where l ranges from 1 to n and r ranges from l to n.

Input Format:
- The first line contains two integers, n (1 <= n <= 250000) and s (1 <= s <= 10^15), representing the number of segments and the maximum length for a piece to be considered small.
- The second line contains n integers a_1, a_2, ..., a_n (1 < a_i < min(s, 10^9)), where a_i is the length of the i-th segment.

Output Format:
- Output the sum of f(l, r) for all possible sub-rods.

Example:
Input:
3 3
1 2 3

Output:
8

Explanation:
f(1,1) + f(1,2) + f(1,3) + f(2,2) + f(2,3) + f(3,3) = 1+1+2+1+2+1 = 8.