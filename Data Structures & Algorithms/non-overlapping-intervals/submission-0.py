class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        min_count = 0
        if not intervals:
            return 0
        sorted_interval = sorted(intervals, key = lambda x:x[1])

        prev = sorted_interval[0]
        for curr in sorted_interval[1:]:
            # if overlap, dont update prev
            if prev[0]<curr[1] and prev[1]>curr[0]:
                min_count+=1

            # else update orev
            else:
                prev = curr
        
        return min_count
        