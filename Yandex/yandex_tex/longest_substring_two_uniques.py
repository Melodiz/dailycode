def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    left, right, ans = 0, 0, 0
    letters = {} 
    while right < len(s):
        letters[s[right]] = right # update
        if len(letters.keys()) > 2: # shrink
            left_most_index = min(letters.values())
            char_to_remove = s[left_most_index]
            left = left_most_index + 1
            del letters[char_to_remove]
        ans = max(ans, right-left+1)
        right += 1
    return ans

# --- Test Cases ---

# Example 1
s1 = "eceba"
print(f"Input: '{s1}', Output: {lengthOfLongestSubstringTwoDistinct(s1)}") # Expected: 3

# Example 2
s2 = "ccaabbb"
print(f"Input: '{s2}', Output: {lengthOfLongestSubstringTwoDistinct(s2)}") # Expected: 5

# Example 3
s3 = "abaccc"
print(f"Input: '{s3}', Output: {lengthOfLongestSubstringTwoDistinct(s3)}") # Expected: 4

# Example 4: Edge Case (Empty String)
s4 = ""
print(f"Input: '{s4}', Output: {lengthOfLongestSubstringTwoDistinct(s4)}") # Expected: 0

# Example 5: Edge Case (Single Character)
s5 = "a"
print(f"Input: '{s5}', Output: {lengthOfLongestSubstringTwoDistinct(s5)}") # Expected: 1

# Example 6: Edge Case (All Same Characters)
s6 = "bbbbbb"
print(f"Input: '{s6}', Output: {lengthOfLongestSubstringTwoDistinct(s6)}") # Expected: 6

# Example 7: Only Two Distinct Characters
s7 = "ababab"
print(f"Input: '{s7}', Output: {lengthOfLongestSubstringTwoDistinct(s7)}") # Expected: 6

# Example 8: All Unique Characters
s8 = "abcdefg"
print(f"Input: '{s8}', Output: {lengthOfLongestSubstringTwoDistinct(s8)}") # Expected: 2

# Example 9: Complex Case
s9 = "aabacbaa"
print(f"Input: '{s9}', Output: {lengthOfLongestSubstringTwoDistinct(s9)}") # Expected: 4

# Example 10: Complex Case
s10 = "abacacacacada"
print(f"Input: '{s10}', Output: {lengthOfLongestSubstringTwoDistinct(s10)}") # Expected: 9
