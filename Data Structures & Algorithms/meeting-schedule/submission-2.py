"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval_sorted = sorted(intervals, key=lambda x: x.start)
        # traverse array. 
        if not intervals:
            return True
        prev = interval_sorted[0]
        for curr in interval_sorted[1:]:
            if prev.end >curr.start:
                return False

            prev = curr
        return True
