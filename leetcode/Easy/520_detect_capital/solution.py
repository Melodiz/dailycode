# Solution for https://leetcode.com/problems/detect-capital/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper(): 
            cnt = 1
            for i in range(1, len(word)):
                if word[i].isupper(): cnt += 1
            return True if cnt == len(word) or cnt == 1 else False
        else:
            return word == word.lower()
        

def run_tests():
    solution = Solution()
    passed, failed = 0, 0
    
    # Test cases: (input_args, expected_output)
    test_cases = [
        ("USA", True),
        ("FlaG", False),
    ]
    
    for test_input, expected in test_cases:
        try:
            result = solution.detectCapitalUse(test_input)
            
            if expected is not None:
                if result == expected:
                    passed += 1
                else:
                    failed += 1
                    print(f"✗ FAIL: Input={test_input}, Expected={expected}, Got={result}")
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
