
# A. Average Height

| Time Limit | 5 seconds |
| :--- | :--- |
| **Memory Limit** | **256 MB** |
| **Input** | **Standard Input** |
| **Output** | **Standard Output** |

Aristarchus is developing dinosaur mascot costumes, and one of the main problems he faces is the varying heights of people. Mascot costumes are not a top-selling item, so they are made in one size, for the "average height". Unfortunately, "average height" is a relative concept.

In search of inspiration, Aristarchus looks out his window, which overlooks a trendy burger joint with a queue of people. Sometimes a person arrives and joins the end of the queue, and sometimes a person from the front of the queue leaves to enter the burger joint. The height of each arriving person is known. After each event (a person arriving or leaving), Aristarchus counts how many people in the queue have a height that exactly matches the average height of all the people currently in the queue.

Aristarchus is a creative person, and arithmetic is not his strong suit. Therefore, you are to write a program that will determine the number of people whose height exactly matches the average height of all people in the queue after each event (a person arriving or leaving the queue).

At the beginning of the observation, there are no people in the queue. At the end of the observation, there may still be people left in the queue.

## Input Format

The first line contains the number of events $N$ ($1 \le N \le 1,000,000$).

The next $N$ lines describe the events. There are two types of events:
* `"+K"` — a person with height $K$ joined the queue. $K$ is an integer, ($1 \le K \le 10^{13}$).
* `"-"` — a person from the front of the queue left for the burger joint.

## Output Format

For each event, print the number of people in the queue whose height exactly matches the average height of all people in the queue.

## Example

### Input
```
10
+ 181
+ 184
+ 183
+ 184
-
-
-
+ 175
+ 175
-
```

### Output
```
1
0
0
0
1
1
0
0
2
```