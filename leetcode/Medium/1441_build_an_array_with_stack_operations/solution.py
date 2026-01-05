# Solution for https://leetcode.com/problems/build-an-array-with-stack-operations/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        head, i = 1, 0
        ans = []
        while i < len(target):
            if head == target[i]:
                ans.append('Push')
                head += 1
                i += 1
            else:
                ans.append('Push')
                ans.append('Pop')
                head += 1
        return ans
        

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([1,3], None, "Example 1"),  # TODO: Add expected output
        (3, None, "Example 2"),  # TODO: Add expected output
        ([1,2,3], None, "Example 3"),  # TODO: Add expected output
        (3, None, "Example 4"),  # TODO: Add expected output
        ([1,2], None, "Example 5"),  # TODO: Add expected output
        (4, None, "Example 6"),  # TODO: Add expected output
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.buildArray(test_input)
            
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
