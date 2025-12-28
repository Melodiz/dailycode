# Solution for https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_window = {}
        left, right, ans = 0,0,0
        while right < len(s):
            if s[right] not in current_window or current_window[s[right]]<left: 
                ans = max(ans, right-left+1)
                current_window[s[right]] = right
            else:
                ans = max(ans, right-left)
                left = current_window[s[right]] + 1
                current_window[s[right]] = right 
            right += 1
        return max(ans, right-left) 

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ("abcabcbb", 3, "Example 1"),
        ("bbbbb", 1, "Example 2"),
        ("pwwkew", 3, "Example 3"),
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.lengthOfLongestSubstring(test_input)
            
            if expected is not None:
                status = "✓ PASS" if result == expected else "✗ FAIL"
                print(f"{name}: {status}")
                print(f"  Input:    {test_input}")
                print(f"  Expected: {expected}")
                print(f"  Got:      {result}")
            else:
                print(f"{name}:")
                print(f"  Input:  {test_input}")
                print(f"  Output: {result}")
        except Exception as e:
            print(f"{name}: ✗ ERROR")
            print(f"  Input: {test_input}")
            print(f"  Error: {e}")
        print()

if __name__ == "__main__":
    run_tests()
