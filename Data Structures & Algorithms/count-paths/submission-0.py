class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for j in range(n)] for i in range(m)]
        # init dp:
    
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i ==0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] =1
        # Traverse DP to fill next cells. 
        # travel either down or right. so cell = result of left cell + top cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]
                

        