class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #Brute force - making a new array and then finding odd and even medians 
        #not optimal at all


        new = nums1 + nums2 
        newLen = len(new)
        new.sort()

        
        if newLen % 2 != 0:
            return new[newLen // 2]
        else:
            return (new[newLen // 2 - 1] + new[newLen // 2]) / 2.0
        