"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x:x.start)

        def isOverlap(interval1, interval2):
            if interval2.start < interval1.end:
                return True

        l, r = 0, 1
        while l < r and r < len(intervals):
            if isOverlap(intervals[l], intervals[r]):
                return False
            l += 1
            r += 1
        
        return True