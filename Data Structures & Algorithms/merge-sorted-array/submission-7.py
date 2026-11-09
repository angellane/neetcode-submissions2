class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1.sort()
        while 0 in nums1:
            nums1.pop(0)
        for i in range(max(len(nums1), len(nums2))):
            for num in nums2:
                nums1.append(num)

        nums2.sort()

        return nums1

            
