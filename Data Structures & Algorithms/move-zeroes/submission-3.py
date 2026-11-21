class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, 0

        while l < len(nums):
            if nums[l] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                r += 1
            l += 1

            

        
         