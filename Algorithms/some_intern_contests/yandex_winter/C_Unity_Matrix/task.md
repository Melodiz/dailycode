1. **Problem Name**: Единичечная матрица

2. **Constraints**:
   - Time Limit: 1 second
   - Memory Limit: 64.0 MB

3. **Input/Output**:
   - Input is provided via standard input or a file named `input.txt`.
   - Output should be written to standard output or a file named `output.txt`.

4. **Matrix Definition**:
   - A square matrix is called a "unity matrix" if it satisfies the following conditions:
     - The sum of the squares of its elements is 1.
     - Its trace (the sum of the elements on the main diagonal) is 1.
     - Its rank is 1.

5. **Task**:
   - Reconstruct the unity matrix given its first row.

6. **Input Format**:
   - The first line contains an integer `n` (1 < n < 100), the size of the matrix.
   - The second line contains `n` real numbers, representing the first row of the matrix.

7. **Output Format**:
   - Output the sum of the elements of the reconstructed matrix with a precision of 10^-3.

8. **Example**:
   - **Input**:
     ```
     2
     0.2 0.4
     ```
   - **Output**:
     ```
     1.8
     ```

9. **Notes**:
   - The trace of a matrix is the sum of the elements on its main diagonal.
   - The rank of a matrix is the maximum number of linearly independent rows (or columns). It is also the highest order of any non-zero minor and the dimension of the image of the linear operator corresponding to the matrix.
