class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        # logic: 1 d dp. each element stores min coins needed to reach the amount. 
        # 0,1,2,3,4...amount
        # at each, check from starting to end. i need to check if the given coing exists. # one
        # one check that it can store the index as 1 if coin exist and check index. O(n)
        # then for the loop of populating the dp.check the loop na dproceed with operatios. 
        dp = [float('inf')] *(amount +1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins: 
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1+dp[i-coin])
                
        return dp[amount] if dp[amount] <float('inf') else -1