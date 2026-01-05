# Solution for https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, x in enumerate(prices):
            flag = True
            for j in range(i+1, len(prices)):
                if x >= prices[j]: 
                    ans.append(x-prices[j])
                    flag = False; break
            if flag:
                ans.append(x)
        return ans
        

def run_tests():
    solution = Solution()
    
    test_cases = [
        ([8,4,6,2,3], [4,2,4,2,3], "Example 1"),
        ([1,2,3,4,5], [1,2,3,4,5], "Example 2"),
        ([10,1,1,6], [9,0,1,6], "Example 3"),
    ]
    
    for test_input, expected, name in test_cases:
        try:
            result = solution.finalPrices(test_input)
            
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
