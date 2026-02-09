# Solution for https://leetcode.com/problems/separate-squares-i/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for x, y, l in squares)
        
        def get_area_below(h):
            area = 0
            for x, y, l in squares:
                if h > y:
                    area += l * min(l, h - y)
            return area

        low = min(y for x, y, l in squares)
        high = max(y + l for x, y, l in squares)
        
        while abs(low-high) > 1e-5:
            mid = (low + high) / 2
            if get_area_below(mid) * 2 < total_area:
                low = mid
            else:
                high = mid
                
        return low

def run_tests():
    solution = Solution()
    passed, failed = 0, 0
    
    # Test cases: (input_args, expected_output)
    test_cases = [
        ([[0,0,1],[2,2,1]], 1.00000),
        ([[0,0,2],[1,1,1]], 1.16667),
    ]
    
    for test_input, expected in test_cases:
        try:
            result = solution.separateSquares(test_input)
            
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
