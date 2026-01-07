# Solution for https://leetcode.com/problems/time-needed-to-buy-tickets/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = tickets[k]
        for i, x in enumerate(tickets):
            if i == k: continue
            elif i < k:
                total_time += min(x, tickets[k])
            else:
                total_time += min(x, tickets[k]-1)
        return total_time
        

def run_tests():
    solution = Solution()
    passed, failed = 0, 0
    
    # Test cases: (input_args, expected_output)
    test_cases = [
        (([2,3,2], 2), 6),
        (([5,1,1,1], 0), 8),
    ]
    
    for test_input, expected in test_cases:
        try:
            if isinstance(test_input, tuple):
                result = solution.timeRequiredToBuy(*test_input)
            else:
                result = solution.timeRequiredToBuy(test_input)
            
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
