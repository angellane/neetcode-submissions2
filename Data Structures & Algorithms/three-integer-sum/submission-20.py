class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0
        
        for i in range(len(nums)):
            
            l, r = i + 1, len(nums) - 1 #i is our anchor, l and r are pointers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                if triplet < 0:
                    l += 1
                elif triplet > 0:
                    r -= 1
                else:
                    if [[nums[i], nums[l], nums[r]]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l+=1
        return res


        

        