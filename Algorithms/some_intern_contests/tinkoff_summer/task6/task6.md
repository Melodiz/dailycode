## Problem Description
You have an array of integers representing heights of people standing in a row. In each step, two adjacent people meet, and then leave the row. After each meeting, the left and right parts of the row are shifted to close the gap. This process continues until there is at most one person left in the row.

The goal is to find the maximum possible sum of absolute differences between the heights of people who meet.

## Input Format
The first line contains an integer n — the number of people (2 ≤ n ≤ 3·10^5).

The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) — the heights of the people.

## Output Format
Output a single integer — the maximum possible sum of absolute differences between the heights of people who meet.