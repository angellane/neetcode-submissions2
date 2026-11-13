class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        prev, curr = 0, 1
        i = 0

        while i <= len(nums):
            if nums[prev] == nums[curr]:
                nums.pop(curr)    
            else:
                prev = curr
                curr = i
                i+=1
        return len(nums)
        