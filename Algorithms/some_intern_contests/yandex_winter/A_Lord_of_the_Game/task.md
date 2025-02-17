1. **Problem Name**: A. Lord of the Game

2. **Constraints**:
   - Time Limit: 1 second
   - Memory Limit: 64.0 MB

3. **Input/Output**:
   - Input is provided via standard input or a file named `input.txt`.
   - Output should be written to standard output or a file named `output.txt`.

4. **Game Description**:
   - There are `N` piles of stones, each with a positive number of stones.
   - Emci selects a pile with the minimum number of stones.
   - Raid selects a pile with the maximum number of stones.
   - The score `S` is the sum of stones in the segment between the piles chosen by Emci and Raid, inclusive.

5. **Objective**:
   - Determine the maximum score `S` that can be achieved if both players play optimally.

6. **Input Format**:
   - The first line contains a single integer `n` (1 < n < 10^5), the number of piles.
   - The second line contains `n` positive integers representing the number of stones in each pile.

7. **Output Format**:
   - Output a single integer, the maximum score `S` that can be achieved.

This problem requires finding the optimal positions for Emci and Raid to maximize the sum of stones between their chosen piles. The solution involves identifying the minimum and maximum values in the list of piles and calculating the sum of stones between these positions.

8. **Examples**

Example 1
Input:
5
5 2 1 4 1
Output:
13

Пример 2
Input:
1
10
Output:
10

Примечания:

В первом наборе входных данных минимальное число камней в кучке равно 1, максимальное число камней в кучке равно 5. Райд может выбрать только кучку под номером 1, а Эмси кучку под номером 3 или под номером 5. Если Эмси выберет кучку 3, то результат игры S=5+2+1=8, а если кучку 5, то - 5+2+1+4+1=13. Максимальный результат среди всех возможных вариантов равен 13.

Во втором наборе входных данных A и B = 10. Эмси и Райд могут выбрать только кучку под номером 1, поэтому ответ на задачу равен 10.
