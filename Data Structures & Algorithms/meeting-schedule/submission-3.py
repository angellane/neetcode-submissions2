"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        busy = set()
        for meeting in intervals:
            for slot in range(meeting.start, meeting.end - 1):
                if slot in busy:
                    return False
                busy.add(slot)
        return True

