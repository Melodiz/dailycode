# Solution for https://leetcode.com/problems/license-key-formatting/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        s = s.replace('-', '')
        i = len(s)-1
        p = 0
        while i >= 0:
            if p > 0 and p % k == 0:
                ans.append('-')
            ans.append(s[i].upper())
            i -= 1
            p += 1
        return ''.join(x for x in ans[::-1])

def run_tests():
    solution = Solution()
    passed, failed = 0, 0

    # Test cases: (input_args, expected_output)
    test_cases = [
        (("5F3Z-2e-9-w", 4), "5F3Z-2E9W"),
        (("2-5g-3-J", 2), "2-5G-3J"),
    ]

    for test_input, expected in test_cases:
        try:
            result = solution.licenseKeyFormatting(*test_input)

            if expected is not None:
                if result == expected:
                    passed += 1
                else:
                    failed += 1
                    print(
                        f"✗ FAIL: Input={test_input}, Expected={expected}, Got={result}")
            else:
                print(f"Output: {result} (Input: {test_input})")
        except Exception as e:
            failed += 1
            print(f"✗ ERROR: Input={test_input}, Error={e}")

    if failed == 0 and passed > 0:
        print("OK")
    elif passed == 0 and failed == 0:
        print("No test cases to run")


if __name__ == "__main__":
    run_tests()
