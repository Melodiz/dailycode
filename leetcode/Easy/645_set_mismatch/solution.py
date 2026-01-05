# Solution for https://leetcode.com/problems/set-mismatch/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = set(x for x in range(1, len(nums)+1)) - set(nums)
        seen = set()
        for x in nums:
            if x in seen: 
                return [x, missing.pop()]
            seen.add(x)


def run_tests():
    solution = Solution()
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([1,2,2,4], None, "Example 1"),  # TODO: Add expected output
        ([1,1], None, "Example 2"),  # TODO: Add expected output
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.findErrorNums(test_input)
            
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
