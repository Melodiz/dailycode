class Solution:
    def climbStairs(self, n: int) -> int:
        return
    
    
    def rec(self, n):
        if n <= 2:
            return 1
        return Solution.rec(Solution, n-1) + Solution.rec(Solution, n-2)