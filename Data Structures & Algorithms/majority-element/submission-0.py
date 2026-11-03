class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        res = nums[len(nums) // 2]
        return res
        