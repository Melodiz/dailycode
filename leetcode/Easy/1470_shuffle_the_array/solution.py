# Solution for https://leetcode.com/problems/shuffle-the-array/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans, n = [], len(nums)//2
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
        

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([2,5,1,3,4,7], None, "Example 1"),  # TODO: Add expected output
        (3, None, "Example 2"),  # TODO: Add expected output
        ([1,2,3,4,4,3,2,1], None, "Example 3"),  # TODO: Add expected output
        (4, None, "Example 4"),  # TODO: Add expected output
        ([1,1,2,2], None, "Example 5"),  # TODO: Add expected output
        (2, None, "Example 6"),  # TODO: Add expected output
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.shuffle(test_input)
            
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
