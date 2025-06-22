## C. Grandpa Egor

**Time Limit:** 2 seconds
**Memory Limit:** 256 MB
**Input:** Standard input or input.txt
**Output:** Standard output or output.txt

Grandpa Egor's family is a very large family that lives in different cities and countries. Once, all family members gathered to congratulate Grandpa Egor on his birthday, but in 2020 it was decided that communicating via video calls would be safer.

Each family home has a certain number of rooms with devices that can be used to organize a video conference for several family members from other cities. These rooms greatly facilitate communication: several family members work remotely and regularly communicate with colleagues in various chats, so at any time of the day they can stay in touch. All relatives want to share news with each other, so the family has a call schedule so that each participant can communicate at the right time.

You are given $m$ queries about the availability of rooms in all homes on the day of the family meeting, and at what time $T$ the family meeting should be held for relatives from different cities. For each query, you need to choose an appropriate set of time slots (in each location, you need to choose one room, and these rooms must be free at time $T$) so that there is no suitable room.

**Please note:** Queries are independent of each other. That is, the answer to one query does not affect the occupancy of a room.

### Input Format

The first line contains an integer $c$ ($2 \le c \le 16$) — the number of homes.

Next follow $c$ blocks of home descriptions. The first line of each block contains the home name, where the family lives, and the number of rooms $n_i$ ($1 \le n_i \le 100$).
Then follow $n_i$ lines, in which the booking schedule for room $r_{ij}$ and its name $s_{ij}$ are given. The schedule $r_{ij}$ is a string of 24 characters, the $k$-th character is equal to 'X' if the $k$-th hour of the day is unavailable for booking, or '.' if it is available.

The next line contains an integer $m$ ($1 \le m \le 1000$) — the number of queries. For each of the following $m$ queries, first comes time $T$ ($0 \le T \le 23$) — the hour of the meeting, followed by $k$ city names where the meeting should be organized in one room. City names are separated by single spaces.

Room names do not repeat. City names do not repeat. City names and room names are continuous strings consisting of Latin alphabet letters, up to 10 characters long.

### Output Format

For each of the $m$ queries, output a message `Yes` (without quotes) and the name of the room where the meeting can be organized, or output the message `No` (without quotes) if it is impossible to find a suitable room.

Rooms in each answer can be output in any order. If there are multiple possible answers to a query, you are allowed to output any suitable one.

### Test Cases

**Input 1:**
```
3
Moscow 2
XXXXXXXX.X.X.X.X.X.XXXXX Kvartal
XXXXXXXXX.X.X.X.X.X.XXXX Kvartet
Minsk 1
XX.XXXXX........XXXXXXXX Toloka
Berlin 2
XX..XXXXXXXXXXXXXXXXXXXX Mitte
XXXXXXXXXXXXXXXX.....XXX Lustgarten
4
3 Moscow Minsk Berlin
2 Moscow Minsk
2 Minsk Berlin
2 Moscow Berlin
```

**Output 1:**
```
No
Yes Kvartal Toloka
Yes Toloka Mitte
Yes Kvartal Lustgarten
```

**Input 2:**
```
3
Moscow 1
XXXXXXXX...........XXXXX Kvartal
Minsk 1
XXXXXXX...........XXXXXX Toloka
Berlin 1
XXXXXX...........XXXXXXX Mitte
1
3 Moscow Minsk Berlin
```

**Output 2:**
```
Yes Kvartal Toloka Mitte
```