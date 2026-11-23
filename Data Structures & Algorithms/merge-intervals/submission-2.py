class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        currBounds = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= currBounds[1]:
                currBounds = [min(intervals[i][0], currBounds[0]), max(intervals[i][1], currBounds[1])]
            else:
                res.append(currBounds)
                currBounds = intervals[i]
        res.append(currBounds)
        return res
        