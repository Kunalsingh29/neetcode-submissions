class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def rob_linear(nums_1:list[int]) -> int:
            if not nums_1:
                return 0
            if len(nums_1) == 1:
                return nums_1[0]
            n = len(nums_1)
            prev2 = nums_1[0]
            prev1 = max(nums_1[0], nums_1[1])

            for i in range(2, n):
                cost = max(nums_1[i] + prev2, prev1)
                prev2 = prev1
                prev1 = cost
            
            return prev1
 
        return max(rob_linear(nums[1:]),rob_linear(nums[:-1]))