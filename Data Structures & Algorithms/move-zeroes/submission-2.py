class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        stack = []

        for num in nums:
            if num != 0:
                stack.append(num)
        for num in nums:
            if num == 0:
                stack.append(num)
        nums[:] = stack
        #extra space is required for this solution
        
        
       
        