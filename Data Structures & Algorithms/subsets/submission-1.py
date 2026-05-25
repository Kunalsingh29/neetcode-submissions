class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         # my approach has been of just trying to reach to correct answer and not exactly understand it. 
         # now we will try to execute the solution in one go by dry running so that we dont ghave to multipple times modify algo and we are able to identify gaps

         # this is a backtracking algo. can be done using DFS. 
         # res
        res = []
        subset = []
        def dfs(i):
            # base case: 
            if i >=len(nums):
                # this subset is being actively modified and each ppend will have a different subset. 
                res.append(subset.copy())
                return

        
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res