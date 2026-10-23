class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        # got the way to track max so far and min so far. product depends on max and min so far to give max 
        # product sub array. so use both. 
        # 2 different arrays to track these. 
        n = len(nums)
        
        
        # max_so_far[0] = nums[0]
        # min_so_far[0] = nums[0]
        res = nums[0]
        
        prev_max = nums[0]
        prev_min = nums[0]
        for i in range(1, n):
            # for each element, calculate 3, store the max in max, min in min 
            num1 = max(nums[i]*prev_max, nums[i]*prev_min, nums[i])
            num2 = min(nums[i]*prev_max, nums[i]*prev_min, nums[i])
            res = max(res, num1)
            prev_max = num1
            prev_min = num2
            #dp[i] = max_so_far[i]

        return res



