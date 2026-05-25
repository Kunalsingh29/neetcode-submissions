class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        
        nums.sort()
        def backtrack(i, suubset):

            if i == len(nums):
                result.append(subset[::])
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            backtrack(i+1, subset)

        backtrack(0, subset)
        return result

