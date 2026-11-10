class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        totalLen = len(nums1) + len(nums2) #We want this so we can iterate until we reach this point in both arrays, that will be median 
        midPoint = totalLen // 2 + 1 #Would this give us the index of the median?
        i, j = 0, 0 #initial pointers 
        curr = 0
        prev = 0
        res = 0
        count = 0

        #If the length of the two is odd then the median is midPoint otherwise it is ((midPoint - 1) + midPoint) / 2)
        while count < midPoint and i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                prev = curr
                curr = nums1[i]
                i += 1
            else:
                prev = curr
                curr = nums2[j]
                j += 1
            count+=1
        if totalLen % 2 != 0:
            res = curr
        else:
            res = (prev + curr) / 2
        return res



        


        