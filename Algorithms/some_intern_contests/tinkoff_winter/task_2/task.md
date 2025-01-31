### Problem Statement

You are given a sequence of days, and for each day, you have a specific budget. Your task is to determine the maximum amount of money that can be spent on purchasing exactly three distinct items, where each item has a cost that is a power of 2. If it is not possible to purchase three distinct items within the given budget, return -1 for that day.

### Input

- An integer \( n \) representing the number of days.
- A list of integers \( a_i \) for \( i = 1 \) to \( n \), where each \( a_i \) is the budget available on the \( i \)-th day.

### Output

- For each day, output the maximum sum of costs of three distinct items that can be purchased within the budget \( a_i \), or -1 if it is not possible to purchase such a combination.

### Constraints

- \( 1 \leq n \leq 10^5 \)
- \( 1 < a_i < 10^{18} \)

### Example

#### Input
```
3
15
67
5
```

#### Output
```
14
67
-1
```

### Explanation

- On the first day, with a budget of 15, the maximum sum of costs for three distinct items is 14 (using items with costs \(2^1\), \(2^2\), and \(2^3\)).
- On the second day, with a budget of 67, the maximum sum is 67 (using items with costs \(2^0\), \(2^1\), and \(2^6\)).
- On the third day, with a budget of 5, it is not possible to purchase three distinct items, so the output is -1.