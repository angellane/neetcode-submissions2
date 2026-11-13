class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        count = 0

        i, j = 0, 0
        midpoint = (len(nums1) + len(nums2)) // 2
        prev, curr = 0, 0 

        totalLen = len(nums1) + len(nums2)

        while count < (midpoint) + 1:
            if i == len(nums1):
                prev = curr
                curr = nums2[j]
                j+=1
            elif j == len(nums2):
                prev = curr
                curr = nums1[i]
                i +=1
            elif nums1[i] < nums2[j]:
                prev = curr
                curr = nums1[i]
                i+=1
            else:
                prev = curr
                curr = nums2[j]
                j+=1
            count += 1

        if totalLen % 2 != 0:
            res = curr 
        else:
            res = (curr + prev) / 2
        return res

        