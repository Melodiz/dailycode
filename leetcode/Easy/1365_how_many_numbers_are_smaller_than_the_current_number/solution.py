# Solution for https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        mp = {}
        for i, x in enumerate(s):
            if x not in mp:
                mp[x] = i
        for i, x in enumerate(nums):
            nums[i] = mp[x]
        return nums

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([8,1,2,2,3], [4,0,1,1,3], "Example 1"),  # TODO: Add expected output
        ([6,5,4,8], [2,1,0,3], "Example 2"),  # TODO: Add expected output
        ([7,7,7,7], [0,0,0,0], "Example 3"),  # TODO: Add expected output
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.smallerNumbersThanCurrent(test_input)
            
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
