# https://leetcode.com/problems/minimum-falling-path-sum/?envType=daily-question&envId=2024-01-19

class Solution:
    def minFallingPathSum(self, A) -> int:
        n = len(A)
        if n == 1:
            return A[0][0]
        dp = [[float('inf')] * n for _ in range(n)]
        ans = float('inf')

        for i in range(len(A)):
            ans = min(ans, self.minFallingPathSumHelper(A, 0, i, dp))

        return ans

    def minFallingPathSumHelper(self, A, row, col, dp):
        m, n = len(A), len(A[0])

        if dp[row][col] != float('inf'):
            return dp[row][col]

        if row == m - 1:
            return A[row][col]

        left = right = float('inf')

        if col > 0:
            left = self.minFallingPathSumHelper(A, row + 1, col - 1, dp)

        straight = self.minFallingPathSumHelper(A, row + 1, col, dp)

        if col < n - 1:
            right = self.minFallingPathSumHelper(A, row + 1, col + 1, dp)

        dp[row][col] = min(left, min(straight, right)) + A[row][col]

        return dp[row][col]


matrix = [[82, 81], [69, 33]]
print(Solution.minFallingPathSum(Solution, matrix))
