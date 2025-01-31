Task: Minimum Operations to Satisfy Divisibility Conditions

You are given a sequence of n integers a1, a2, ..., an and three positive integers x, y, and z.

Your task is to find the minimum number of operations needed to satisfy the following conditions:
1. At least one element in the sequence is divisible by x
2. At least one element in the sequence is divisible by y
3. At least one element in the sequence is divisible by z

In one operation, you can choose any element ai (1 ≤ i ≤ n) and increase it by 1.

Note: It's allowed for the same element to satisfy multiple divisibility conditions.

Input:
- The first line contains four integers: n (1 ≤ n ≤ 2*10^5), x, y, z (1 < x, y, z ≤ 10^6)
- The second line contains n integers: a1, a2, ..., an (1 ≤ ai ≤ 10^18)

Output:
- A single integer representing the minimum number of operations required to satisfy all conditions.

Example:
Input:
6 10 20 30
8 17 5 28 39 13

Output:
3

Comment on the example
In the example, you can increase a4 twice and increase a5 once. Then a4 will be divisible by 10, a5 will be divisible by 20, and a4 will be divisible by 30.