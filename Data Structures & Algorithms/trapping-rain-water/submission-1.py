class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        #I want to find the minimum of 2 bars, then if they have space between them count that, continue for every bar in the list and then add up all the space 

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]


        return res


            
        