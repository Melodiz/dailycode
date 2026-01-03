# Solution for https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        A = B = 6

        for _ in range(2, n + 1):
            A, B = (2*A + 2*B) % MOD, (2*A + 3*B) % MOD

        return (A + B) % MOD

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        (1, None, "Example 1"),  # TODO: Add expected output
        (5000, None, "Example 2"),  # TODO: Add expected output
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.numOfWays(test_input)
            
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
