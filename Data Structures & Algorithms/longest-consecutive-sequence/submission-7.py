class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        length = 0
        if not nums:
            return 0
        for n in nums:
            if n + 1 in numSet:
                length += 1
        return length
        