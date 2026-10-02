class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l, r = 0, len(nums) - 1
        if not nums:
            return []

        while l < r:
            if nums[l] + nums[r] > target:
                r-=1
            elif nums[l] + nums[r] < target:
                l+=1
            else:
                return [l, r]
        