class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        res = []
        
        currBounds = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= currBounds[1]:
                currBounds = [min(currBounds[0], intervals[i][0]), max(currBounds[1], intervals[i][1])]
            else:
                res.append(currBounds)
                currBounds = intervals[i]
        res.append(currBounds)



        return res
                

        