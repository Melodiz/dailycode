# Metro Schedule Problem

## Problem Statement

Egor and his friends were walking around city N and found a metro map. In this city, there are n metro lines, each with its own schedule. After studying the schedule, they discovered that on line i, the first train starts running at a_i seconds from the beginning of the day, and each new train starts its route after the previous one with an interval of b_i seconds. Now they want to learn how to determine, for a given line and time, when they will see a train after arriving at the station.

## Input Format

- The first line contains an integer n — the number of metro lines in the city (1 ≤ n ≤ 100).
- The next n lines contain two integers each: a_i, b_i — the time when the first train on the i-th line arrives at the station, and the interval between trains (0 ≤ a_i < b_i ≤ 10^9).
- The next line contains an integer q — the number of queries (1 ≤ q ≤ 100).
- The next q lines contain two integers each: t_i, d_i — the line number and the time when friends arrive at the station (1 ≤ t_i ≤ n, 1 ≤ d_i ≤ 10^9).

## Output Format

For each query, output the answer to the problem on a separate line.

## Example

### Input:
```
3
0 1
2 3
1 4
5
1 2
2 6
3 6
2 5
3 8
```

### Output:
```
2
8
9
5
9