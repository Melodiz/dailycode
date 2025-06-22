
## B. Zokori

**Time Limit:** 1 second
**Memory Limit:** 256 MB
**Input:** Standard input
**Output:** Standard output

Modern zokori are rather harmless rodents, but ancient zokori could well have changed the geological structure of the entire Earth. Scientists found frightening bloodsucking mosquitoes in Baltic amber with fragments of their DNA. They identified 10 markers found in zokori DNA and denoted them with letters C, D, E, F, G, H, I, J, K, L.

In total, they identified $N$ DNA fragments, and now for further research, they need to count the number of pairs of fragments that have at least one common marker.

### Input Format

The first line contains an integer $N$ ($1 \le N \le 500,000$) — the number of DNA fragments.

The following $N$ lines describe each DNA fragment: a string consisting of no more than 10 characters from C to L. Markers within a fragment can repeat. Different fragments can contain the same markers in the same order.

### Output Format

Output a single number: the count of pairs of fragments that have at least one common marker.

### Example

**Input:**
```
5
DC
JG
GJ
JJ
FCD
```

**Output:**
```
4
```

**Notes:**
Fragment pairs forming:
DC - FCD
JG - JJ
JG - JJ
GJ - JJ