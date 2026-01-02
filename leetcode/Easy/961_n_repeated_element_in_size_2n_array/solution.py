# Solution for https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        was = set()
        for x in nums:
            if x in was: return x
            was.add(x)
        return         

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([1,2,3,3], 3, "Example 1"),  # TODO: Add expected output
        ([2,1,2,5,3,2], 2, "Example 2"),  # TODO: Add expected output
        ([5,1,5,2,5,3,5,4], 5, "Example 3"),  # TODO: Add expected output
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.repeatedNTimes(test_input)
            
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
