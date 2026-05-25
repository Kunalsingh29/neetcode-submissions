class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        def dfs(index, path):
            res.append(path[:])

            for i in range(index, n):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        
        dfs(0, [])
        return res
