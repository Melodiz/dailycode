1. **Problem Name**: В. Вася и котики

2. **Constraints**:
   - Time Limit: 1 second
   - Memory Limit: 64.0 MB

3. **Input/Output**:
   - Input is provided via standard input or a file named `input.txt`.
   - Output should be written to standard output or a file named `output.txt`.

4. **Problem Description**:
   - Vasia has `n` cats and `m` beds with integer coordinates.
   - The happiness of each cat is defined as the distance to the nearest bed occupied by another cat.
   - Some cats are picky and want to sleep on specific beds.
   - Vasia wants to arrange the cats such that the minimum happiness among all cats is maximized.

5. **Input Format**:
   - The first line contains three integers `n`, `m`, and `k` (2 < n < m < 105, 0 < k < n), representing the number of cats, beds, and already occupied beds, respectively.
   - The second line contains `m` positive integers representing the coordinates of the beds. All coordinates are distinct.
   - The third line contains `k` positive integers representing the coordinates of the already occupied beds. These coordinates are a subset of the bed coordinates.

6. **Output Format**:
   - Output a single integer, the maximum possible value of the minimum happiness among all cats.

7. **Examples**:
   - **Example 1**:
     - Input:
       ```
       2 4 1
       1 5 6 9
       6
       ```
     - Output:
       ```
       5
       ```
   - **Example 2**:
     - Input:
       ```
       3 5 0
       1 7 3 4 2
       ```
     - Output:
       ```
       3
       ```

8. **Notes**:
   - Bed coordinates can be given in any order.
   - Note that `k` can be zero, meaning no beds are initially occupied.
