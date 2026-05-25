class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] # n!
        path = [] # n
        used = [False]*len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
            
            for i in range(len(nums)): # 0-n
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                dfs() # - 1- n-1 = n-1 factorial


                path.pop()
                used[i] = False
            
        dfs()
        return res
        
        
