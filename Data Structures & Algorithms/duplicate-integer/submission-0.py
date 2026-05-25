class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_exist = []
        for x in nums:
            if x in num_exist:
                return True
            else:
                num_exist.append(x)

        return False