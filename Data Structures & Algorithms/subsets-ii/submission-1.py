class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        nums.sort()

        def backtrack(idx, path):
            if len(path)<= n:
                res.append(path[:])
            if idx>=n:
                return
            
            for i in range(idx, n):
                if i >idx and nums[i-1] == nums[i] and i>0:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return res
            
        