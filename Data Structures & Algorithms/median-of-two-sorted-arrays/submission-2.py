class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        merged = nums1 + nums2
        merged.sort()

        lenMerged = len(merged)

        if lenMerged % 2 != 0:
            return merged[lenMerged // 2]
        else:
            return (merged[lenMerged // 2 - 1] + merged[lenMerged // 2]) / 2.0
        