class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search guarantees that our mid point will become the target all the time if the target exists

        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while l <= r:
            if nums[l] < nums[r]:
                break

            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return m if target in nums else -1

        