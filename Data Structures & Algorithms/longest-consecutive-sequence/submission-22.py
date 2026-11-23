class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums.sort()
        res = 1
        count = 1

        for i in range(len(nums)):
            cur = nums[i]
            prev = nums[i - 1]
            if cur == prev + 1:
                count += 1
                res = max(res, count)
            elif cur == prev:
                continue 
            else:
                count = 1
        return res
        