Given an array a1, a2, ..., an. For each p from 1 to k, consider the following process:
1. For all i, j such that 1 < i < j < n, list the pairs (ai, aj);
2. In the resulting sequence, replace each pair with the sum of its elements;
3. In the new sequence, raise each element to the power of p;
4. Sum all the numbers in the final sequence;
5. Replace the result with its remainder when divided by 998244353;
6. Denote the result as f(p).

Find the values f(1), f(2), ..., f(k).

Input format:
The first line contains the numbers n (2 < n ≤ 2 × 10^5) and k (1 ≤ k < 300).
The second line contains the numbers a1, a2, ..., an (1 ≤ ai < 10^8).

Output format:
Output f(1), f(2), ..., f(k), each on a new line.