## F. TV Series Recommendation

| Language | python3.6+numpy+pandas | All languages |
|---|---|---|
| Time Limit | 60 seconds | 300 seconds |
| Memory Limit | 128 MB | 384 MB |
| Input | standard input or input.txt |
| Output | standard output or output.txt |

It is necessary to develop a TV series recommendation system. In this system, each of $U$ users can rate each of $M$ TV series they have watched, with ratings ranging from 1 to $k$. A training dataset is provided, which contains $D$ known ratings. A test dataset is also given, which contains $T$ user-series pairs. For these pairs, you are required to predict what rating the user gave to the series. The true ratings for these pairs are hidden.

You need to predict ratings with an RMSE metric no worse than the prediction of the $SVD^1$ model.

### Input Format

The first line contains integers $k, U, M, D, T$ separated by spaces ($2 \le k \le 100$, $1 \le U, M \le 10000$, $1 \le D, T \le 1000000$).
Then follow $D$ lines of the training dataset. The $i$-th line of the training dataset contains three integers $u_i, m_i$, and $r_i$, where $u_i$ ($0 \le u_i \le U-1$) is the user ID, $m_i$ ($0 \le m_i \le M-1$) is the series ID, $r_i$ ($1 \le r_i \le k$) is the rating that this user gave to this series.
Then follow $T$ lines of the test dataset. The $i$-th line of the test dataset contains $u_i$ and $m_i$, where $u_i$ ($0 \le u_i \le U-1$) is the user ID, $m_i$ ($0 \le m_i \le M-1$) is the series ID. For these lines, you need to predict the ratings.

### Output Format

For each of the $T$ lines of the test dataset, you need to output the predicted rating (a real number) on a separate line.

### Example

**Input:**
```
10 3 3 5 4
0 0 9
0 1 8
1 1 4
1 2 6
2 2 7
0 2
1 0
2 0
2 1
```

**Output:**
```
10.00000
6.00000
7.00000
5.00000
```

### Notes

$^1$ SVD model:

$\hat{r}_{um} = \mu + b_u + b_m + \langle p_u, q_m \rangle$

where $\hat{r}_{um}$ — is the predicted rating for user $u$ and series $m$, $\langle \cdot, \cdot \rangle$ — is the scalar product of vectors, $a, \mu, b_u, b_m, p_u, q_m$ — parameters tuned on the training set, where $\mu, b_u, b_m$ — are numerical parameters, and $p_u, q_m$ — are $d$-dimensional vectors for some $d$. It is recommended to use $d=10$.