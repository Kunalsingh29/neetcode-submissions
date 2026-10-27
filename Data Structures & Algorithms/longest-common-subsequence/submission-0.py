class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ## Tabulation approach : 
        # # create dp. # iof match, increment, if not max of left or top . 
        row, col = len(text1), len(text2)
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

        # init done. to 0. 
        for i in range(1, row+1):
            for j in range(1, col+1):
                # for match
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                #for mismatch: 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[row][col]



        