"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[j].start < intervals[i].start or intervals[j].end < intervals[i].end or intervals[i].start == intervals[j].start:
                    return False
        return True
