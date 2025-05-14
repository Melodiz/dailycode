# Arithmetic Progressions

Today is Oleg's birthday, he turns 10 years old. Since 10 is a special age, his parents gave him a special gift: an array of numbers from 1 to 10. Delighted with such a gift, he immediately began to study its properties.

Recently, during a walk, friends told Oleg about arithmetic progressions. To study the properties of the array, Oleg decided to start with something small, specifically with arithmetic progressions of length 3. Three numbers a, b, c form an arithmetic progression if b - a = c - b. It turned out that not all subarrays can contain such arithmetic progressions, so Oleg decided to first find out how many subarrays exist in which three numbers can be selected, without changing their order, with the required property.

A subarray from l to r is defined as an array of elements A_l, A_{l+1}, ..., A_r.

## Input Format

The first line of input contains the number n - the length of Oleg's array (3 ≤ n ≤ 10^5).

The second line contains n integers A_1, A_2, ..., A_n - the gifted array (1 ≤ A_i ≤ 10).

## Output Format

Output the number of subarrays that interest Oleg.
## Examples

### Example 1:
```
Input:
5
1 2 3 3 2

Output:
3
```

### Explanaition 1:
good subarrays are:
[1, 2, 3, 3, 2] 
[1, 2, 3, 3]
[1, 2, 3]

### Example 2:
```
Input:
6
5 1 3 5 2 5

Output:
6
```

### Explanaition 2:
good subarrays are:
[5, 1, 3, 5]
[5, 1, 3, 5, 2]
[5, 1, 3, 5, 2, 5]
[1, 3, 5]
[1, 3, 5, 2]
[1, 3, 5, 2, 5]

### Example 3:
```
Input:
4 
1 9 2 3

Output: 
1
```
Input:
3
1 3 2

Output:
0
```
