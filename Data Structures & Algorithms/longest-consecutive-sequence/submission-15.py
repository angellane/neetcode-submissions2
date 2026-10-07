class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        res = 0
        for n in nums:
            curr, length = n, 0
            while curr in numSet:
                curr += 1
                length += 1
            res = max(length, res)
        return res

        