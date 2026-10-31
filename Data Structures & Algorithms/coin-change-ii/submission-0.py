class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # logic: dp, table of results. 
        #init table. 
        # traverse table: fill table return last elelemt. 
        row = len(coins) + 1 
        col = amount + 1
        dp = [[0 for _ in range(col)] for _ in range(row)]
        # initialised already to 0. 

        for i in range(row):
            dp[i][0] = 1

        for i in range(1, row):
            for j in range(1, col):
                # for eacl cell, check if amount is valid. then make choice: 
                if j - coins[i-1]>=0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else: 
                    dp[i][j] = dp[i-1][j]

        return dp[row-1][col-1]


