# Solution for https://leetcode.com/problems/last-stone-weight/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            l1 = heapq.heappop(stones) 
            l2 = heapq.heappop(stones)
            result = l1 - l2
            if result != 0:
                heapq.heappush(stones, result)  
        return abs(stones[0]) if stones else 0


def run_tests():
    solution = Solution()
    passed, failed = 0, 0
    
    # Test cases: (input_args, expected_output)
    test_cases = [
        ([2,7,4,1,8,1], 1),
        ([1], 1),
    ]
    
    for test_input, expected in test_cases:
        try:
            result = solution.lastStoneWeight(test_input)
            
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
