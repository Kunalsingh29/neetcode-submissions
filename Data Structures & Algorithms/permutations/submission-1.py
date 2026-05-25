class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        visited = [False]*n

        res = []
        local_ = []

        def backtrack(visit, local_res):

            if len(local_res) == n:
                res.append(local_res[:])
                return

            for i in range(0, n):
                if visited[i]:
                    continue
                visited[i] = True
                local_res.append(nums[i])
                backtrack(visited, local_res)

                local_res.pop()
                visited[i] = False
        
        backtrack(visited, local_)
        return res

                
                
        