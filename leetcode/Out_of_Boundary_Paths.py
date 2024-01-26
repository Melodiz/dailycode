class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # our idea is to find, using dp, number of path to move the ball at the corner of matrix
        # using only n-1 moves;
        data = [[0 for i in range(n+2)] for j in range(m+2)]
        data[startRow+1][startColumn+1] = 1
        dp = data.copy()

        print(f'----{0}----')
        for i in range(n+2):
            print(data[i])

        for iteration in range(maxMove):
            dp[0][0] = dp[1][0] + dp[0][1]
            for k in range(2,m+2):
                
            
            for i in range(n+2):
                for j in range(m+2):
                    

                    
        return
                    
        



print(Solution.findPaths(Solution, 2, 2, 2, 0, 0))


        # print(f'----{-1+1}----')
        # for i in range(n+2):
        #     print(dp[i])

        # for t in range(maxMove-1):
        #     temp = dp.copy()
        #     for i in range(1,n+1):
        #         for j in range(1,m+1):
        #             temp[i][j]+=temp[i-1][j-1]
        #             temp[i][j]+=temp[i+1][j+1]
        #             temp[i][j]+=temp[i+1][j-1]
        #             temp[i][j]+=temp[i-1][j+1]
        #     dp = temp

        #     print(f'----{t+1}----')
        #     for i in range(n+2):
        #         print(dp[i])
                
        # ans = 0
        # for i in range(m):
        #     ans += dp[1][i]
        #     ans += dp[-2][i]
        # for j in range(n):
        #     ans += dp[j][1]
        #     ans += dp[j][-2]

        # return ans
        