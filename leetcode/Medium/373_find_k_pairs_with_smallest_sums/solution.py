# Solution for https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

import heapq
from typing import List, Optional


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while min_heap and len(ans) < k:
            cur_sum, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return ans
        

def run_tests():
    solution = Solution()
    passed, failed = 0, 0
    
    # Test cases: (input_args, expected_output)
    test_cases = [
        (([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]]),
        (([1,1,2], [1,2,3], 2), [[1,1],[1,1]]),
    ]
    
    for test_input, expected in test_cases:
        try:
            result = solution.kSmallestPairs(*test_input)
            
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
