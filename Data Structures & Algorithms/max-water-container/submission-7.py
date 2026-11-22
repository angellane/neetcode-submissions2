class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            curMax = 0
            for j in range(i, len(heights)):
                width = abs(j - i)
                area = min(heights[i], heights[j]) 
                curMax = max(curMax, width * area)
            res = max(curMax, res)
        
        return res
                
                

        