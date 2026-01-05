# Solution for https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(x for x in range(1, len(nums)+1))-set(nums))
    
        

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([4,3,2,7,8,2,3,1], [5,6], "Example 1"),  # TODO: Add expected output
        ([1,1], [2], "Example 2"),  # TODO: Add expected output
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.findDisappearedNumbers(test_input)
            
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
