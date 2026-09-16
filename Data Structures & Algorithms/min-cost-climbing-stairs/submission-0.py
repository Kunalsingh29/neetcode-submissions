class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # logic, recursion memoization. 
        # recur index 0 or 1. 
        # store cost, keep adding cxost when selectingthe index. 
        n = len(cost)
    
        prev1 = cost[1]
        prev2 = cost[0]

        for i in range(2, n):

            cost_ = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = cost_

    
        return min(prev2, prev1)
