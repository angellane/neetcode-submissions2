class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        new = nums1 + nums2
        new.sort()

        newLen = len(new)
        
        if newLen % 2 != 0:
            return new[newLen // 2]
        else:
            return (new[newLen // 2 - 1] + new[newLen // 2]) / 2



        
            
        