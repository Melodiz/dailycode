Task: Minimum Operations to Adjust Range

Given:
- An array A of positive integers with size n (1 ≤ n ≤ 2*10^5)
- A positive integer m (1 ≤ m ≤ n-2)
- Two positive integers l and h, where l may be greater than h initially

Problem:
You are allowed to perform operations on l and h. In each operation, you can either increase or decrease l or h by 1. Your goal is to adjust l and h such that there are at least m numbers in the array A that satisfy the condition l ≤ A[i] ≤ h.

Task:
Determine the minimum number of operations required to adjust l and h to meet the above condition.

Output:
Print a single integer representing the minimum number of operations needed.

Constraints:
- 1 ≤ n ≤ 2*10^5
- 1 ≤ m ≤ n-2
- All elements in array A are positive integers
- l and h are positive integers

Note:
The initial values of l and h may not satisfy l ≤ h. You need to consider this in your solution.