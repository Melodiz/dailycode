## D. Buddha Statuette

**Time Limit:** 3 seconds
**Memory Limit:** 256 MB
**Input:** Standard input or input.txt
**Output:** Standard output or output.txt

Marat came to a long-awaited vacation in Bali and decided to buy a memorable souvenir - a Buddha statuette. There are $n$ statuettes of different types displayed in the souvenir shop, and each statuette of type $i$ costs exactly $i$ units of local currency.

Marat decided that he needed to buy statuettes of all types from 1 to $k$. Fortunately, the seller told Marat that he would receive a discount: if he bought statuettes located in arbitrary places, but in a certain continuous segment (statuettes from position $l$ to $r$ inclusive), he would not need to buy several statuettes of the same type, repeating which he decided to give to friends, relatives, and colleagues after returning home from Bali.

Thus, if, for example, Buddha statuettes are displayed in the order 1 2 2 3 3 1, and Marat wants to buy statuettes of types 1 to 3, he can buy statuettes from the first to the fourth position (in this case, two statuettes of type 2 are bought). And if the statuettes 1 2 5 4 3 are displayed in the shop (again $k=3$), Marat can buy all 5 statuettes.

Help Marat determine the minimum total cost of Buddha statuettes, located consecutively, among which there are statuettes of all types from 1 to $k$.

It is guaranteed that for all test cases, an answer exists.

### Input Format

The first line contains two integers $n$ and $k$ ($1 \le k \le n \le 500,000$).

The second line contains $n$ integers $a_i$ (type of the $i$-th statuette) ($1 \le a_i \le n$) — a description of the Buddha statuettes in the souvenir shop. Statuettes are listed from left to right.

It is guaranteed that for all test cases, an answer exists.

### Output Format

Output a single integer - the minimum total cost in local currency for which Marat could buy the statuettes (without considering the future discount).

### Examples

**Example 1**

**Input:**
```
6 3
1 2 2 3 3 1
```
**Output:**
```
8
```

**Example 2**

**Input:**
```
5 3
1 2 5 4 3
```
**Output:**
```
15
```

**Example 3**

**Input:**
```
6 3
1 2 6 3 3 1
```
**Output:**
```
12
```

**Example 4**

**Input:**
```
6 1
6 2 3 1 2 3
```
**Output:**
```
1
```

**Example 5**

**Input:**
```
7 7
1 2 3 4 6 5 7
```
**Output:**
```
28
```

**Example 6**

**Input:**
```
10 2
1 9 2 4 3 1 8 2 10 9
```
**Output:**
```
10
```