## E. Secrets of Space

**Time Limit:** 2 seconds
**Memory Limit:** 64 MB
**Input:** Standard input or input.txt
**Output:** Standard output or output.txt

A new top-secret Yandex Cosmos service is looking for an ML intern. As the first test task for the candidate, it is proposed to decipher a recently found cryptogram, which contains a formula written for cosmonauts, presumably in the framework of exploring new galaxies. It is possible that the origin of this tablet is extraterrestrial!

It is known that the following inscription is sealed on the tablet:

$f(x) = a \cdot \tan(x) + (b \cdot \sin(x) + c \cdot \cos(x))^2 + d \cdot \sqrt{x}$

Unfortunately, parts of the tablet were lost, and the values of the coefficients $a, b, c, d$ are missing. However, on the reverse side of the tablet, some known values of $x$ and $f(x)$ were found for already existing galaxies.

You have an excellent opportunity to help solve this puzzle by finding the unknown coefficients, and not only get an internship, but also feel like you've made a breakthrough in space exploration.

### Input Format

The first line contains an integer $n$ ($10 \le n \le 1000$) — the number of known values of the function $f(x)$.
The following $n$ lines each contain a pair of real numbers $x$ and $f(x)$, separated by a space.

### Output Format

Output the values of the unknown coefficients $a, b, c, d$ on a single line, separated by spaces, with an accuracy of exactly 2 decimal places.

### Example

**Input:**
```
20
0.5 7.11
1.0 6.69
1.5 4.97
2.0 4.25
2.5 5.75
3.0 8.58
3.5 10.56
4.0 10.26
4.5 8.32
5.0 6.86
5.5 7.54
6.0 10.04
6.5 12.35
7.0 12.62
7.5 10.88
8.0 8.97
8.5 8.91
9.0 10.99
9.5 13.53
10.0 14.42
```
**Output:**
```
0.00 1.00 2.00 3.00
```