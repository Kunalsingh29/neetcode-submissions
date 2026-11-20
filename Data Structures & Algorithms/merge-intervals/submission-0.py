class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sort by starting, then merge by overlap. over lap with current one and not all. ok. current is the bottlenecj. 
        # sort by key. lets see. 
        intervals_s = sorted(intervals, key = lambda x:x[0])

        res = [intervals_s[0]]
        for curr in intervals_s[1:]:
            prev = res[-1]
            last = prev[1]
            if prev[1]>=curr[0] and prev[0]<=curr[1]:
                last = max(prev[1], curr[1])
                res[-1][1] = last

            else:
                res.append(curr)

        return res






