class Solution:
    def trap(self, height: List[int]) -> int:

        


        for i in range(len(height)):
            leftMax = 0
            rightMax = 0
            for l in range(i + 1):
                leftMax = max(leftMax, height[l])
            for r in range(i, len(height)):
                rightMax = max(rightMax, height[r])
            res += min(leftMax, rightMax) - height[i]
        return res
                
                    
                
        
