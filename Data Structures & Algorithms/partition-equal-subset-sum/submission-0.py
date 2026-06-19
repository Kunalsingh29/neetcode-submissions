class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        _sum = 0
        n = len(nums)

        for num in nums:
            _sum+=num
        if _sum%2 != 0:
            return False

        # if even, perform knapsack: 
        target = _sum/2
        rows = n+1
        cols = int(target+1)
        print(target)
        
        dp = [[False for _ in range(cols)] for _ in range(rows)]
        # initialization
        for i in range(rows):
            
            for j in range(cols):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
        
        # subset logic based on target: knapsack:
        for i in range(1, rows):
            for j in range(1, cols):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j]

        return dp[rows-1][cols-1]


        



    

      



        