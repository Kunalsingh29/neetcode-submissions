# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         # array of length n: 
#         # add nbum of ways to it and use it. 
#         res = [-1]*(n+1)
#         def recur(length):
# # memoisation: 

#             # base case: 
#             if length < 0: 
#                 return 0
#             if length == 0:
#                 return 1

#             if res[length]!=-1:
#                 return res[length]
#             else:
#                 res[length] = recur(length -1) + recur(length - 2)
#                 return res[length]

#         return recur(n)

class Solution:
    def climbStairs(self, n: int) -> int:
       # 1 D DP, then fill it
       # indulge in world of programming, get all syntax, do all that i need. cool \
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
       # base case complete: 

       # not travers and fill in O(n)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        
        return dp[n]



            