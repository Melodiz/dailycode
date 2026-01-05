# Solution for https://leetcode.com/problems/largest-rectangle-in-histogram/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_with_sentinel = [0] + heights + [0]
        stack = []
        max_area = 0
        
        for i in range(len(heights_with_sentinel)):
            while stack and heights_with_sentinel[i] < heights_with_sentinel[stack[-1]]:
                h = heights_with_sentinel[stack.pop()]
                left = stack[-1] if stack else 0
                width = i - left - 1
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        return max_area

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([2,1,5,6,2,3], 10, "Example 1"),
        ([2,4], 4, "Example 2"),
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.largestRectangleArea(test_input)
            
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
