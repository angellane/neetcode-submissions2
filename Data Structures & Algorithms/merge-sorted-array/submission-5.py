class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(len(nums1)):
            if 0 in nums1:
                nums1.remove(0)
        

        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()