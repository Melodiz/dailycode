Determine the maximum number of groups of three points that can be formed from n points of 2D plane, where each group forms a non-degenerate triangle. However this triangles can overlap each other. Each point can belong to at most one group (each point can used only in one triangle)

A triangle is non-degenerate if the three points are not collinear.

Input Format:
- The first line contains the integer n (3 < n < 300) — the number of residents.
- Each of the following n lines contains two integers x and y (-10^10 < xi, yi < 10^10) — the coordinates of the house where the i-th person lives.

Output the maximum number of non-degenerate groups of three.

Note: Guaranteed that no two houses are located at the same point.