# Solution for https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i, x in enumerate(tokens):
            if x not in ['*', '-', '+', '/']:
                nums.append(int(x))
            else:
                b, a = nums.pop(), nums.pop()
                if x == '+': nums.append(a+b)
                elif x == '-': nums.append(a-b)
                elif x == '*': nums.append(a*b)
                else: nums.append(int(a/b))
        return int(nums[0])

        

def run_tests():
    solution = Solution()
    
    # Test cases: (input_args, expected_output, test_name)
    test_cases = [
        (["2","1","+","3","*"], 9, "Example 1"),
        (["4","13","5","/","+"], 6, "Example 2"),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22, "Example 3"),
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.evalRPN(test_input)
            
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
