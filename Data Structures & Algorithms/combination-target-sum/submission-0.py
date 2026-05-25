class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
       
        combination = []
        def dfs(i, sum_):
            if sum_ == target:
                res.append(combination.copy())
                return
            elif sum_>target or i == len(candidates):
                return

           
            for j in range(i, len(candidates)):
                combination.append(candidates[j])
                dfs(j, sum_ + candidates[j])
                combination.pop()

        dfs(0, 0)
        return res

    
