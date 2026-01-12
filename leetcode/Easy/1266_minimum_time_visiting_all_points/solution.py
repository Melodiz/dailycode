# Solution for https://leetcode.com/problems/minimum-time-visiting-all-points/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(1, len(points)):
            total_time += max(abs(
                points[i][0]-points[i-1][0]), 
                abs(points[i][1]-points[i-1][1])
                )
        return total_time

def run_tests():
    solution = Solution()
    passed, failed = 0, 0
    
    # Test cases: (input_args, expected_output)
    test_cases = [
        ([[1,1],[3,4],[-1,0]], 7),
        ([[3,2],[-2,2]], 5),
    ]
    
    for test_input, expected in test_cases:
        try:
            result = solution.minTimeToVisitAllPoints(test_input)
            
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
