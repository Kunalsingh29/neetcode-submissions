class Solution:
    def climbStairs(self, n: int) -> int:
        
        # array of length n: 
        # add nbum of ways to it and use it. 
        res = [-1]*(n+1)
        def recur(length):
# memoisation: 

            # base case: 
            if length < 0: 
                return 0
            if length == 0:
                return 1

            if res[length]!=-1:
                return res[length]
            else:
                res[length] = recur(length -1) + recur(length - 2)
                return res[length]

        return recur(n)


            