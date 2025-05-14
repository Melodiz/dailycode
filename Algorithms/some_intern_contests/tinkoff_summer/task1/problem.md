# Almost Palindrome

## Problem Statement

Recently, Kirill found a string of four characters. He became curious whether it is an "almost palindrome". A string is called an "almost palindrome" if it's possible to remove one character from it so that the resulting string reads the same from left to right as from right to left.

Help Kirill check this.

## Input Format

The input consists of a single line containing a string of four Latin characters.

## Output Format

Output "YES" if the string is an almost palindrome, and "NO" otherwise.

## Examples

### Example 1
**Input:**
```
acba
```

**Output:**
```
YES
```

### Example 2
**Input:**
```
dcba
```

**Output:**
```
NO
```

## Solution Approach

To solve this problem, we need to check if removing one character from the string can make it a palindrome. The provided solution uses a two-pointer approach with a flag to allow for one mismatch. If more than one mismatch is found, the string cannot be an almost palindrome.
