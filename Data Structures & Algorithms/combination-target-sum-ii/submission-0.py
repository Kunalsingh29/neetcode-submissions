class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()


        # combination bcode for all elements, start at next element, if newxt element after pop is same, then skip not before adding. 
        def comb_sum(index, path, path_sum):

            if path_sum == target:
                res.append(path[:])
                return

            if path_sum>target:
                return
            
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue    

                path.append(candidates[i])
                path_sum += candidates[i]
                comb_sum(i+1, path, path_sum)

                path.pop()

                path_sum -= candidates[i]
    

        comb_sum(0, [], 0)
        return res
                

