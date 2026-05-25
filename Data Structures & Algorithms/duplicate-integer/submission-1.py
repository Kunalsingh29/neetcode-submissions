class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        for x in nums:
            if x in num_map:
                return True
            else:
                num_map[x] = True

        return False