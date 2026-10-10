class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search guarantees that our mid point will become the target all the time if the target exists

        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
            
        return -1

        