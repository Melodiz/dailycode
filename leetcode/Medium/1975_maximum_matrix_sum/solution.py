# Solution for https://leetcode.com/problems/maximum-matrix-sum/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_el = float('inf')
        count_negative = 0
        s = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                s += abs(matrix[i][j])
                count_negative += matrix[i][j] < 0
                min_el = min(min_el, abs(matrix[i][j]))
        if count_negative % 2 == 0:
            return s
        return s - 2 * min_el


def run_tests():
    solution = Solution()

    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        ([[1, -1], [-1, 1]], 4, "Example 1"),  # TODO: Add expected output
        ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16,
         "Example 2"),  # TODO: Add expected output
    ]

    for test_input, expected, name in test_cases:
        try:
            result = solution.maxMatrixSum(test_input)

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
