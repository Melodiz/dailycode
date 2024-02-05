class Solution:
    def firstUniqChar(self, s: str) -> int:
        alf = 'qwertyuiopasdfghjklzxcvbnm'
        dp = {}
        for char in alf:
            dp[char] = -1
        for i in range(len(s)):
            if dp[s[i]] == -1:
                dp[s[i]] = i
            else:
                dp[s[i]] = -2  
        ans = 10**9
        for char in alf:
            if dp[char] > -1:
                ans = min(ans, dp[char])
            
        if ans < 10**9:
            return ans
        return -1
            