class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        
        prod1 = 1 
        for i in range(len(nums)):
            res[i] = prod1
            prod1 *= nums[i]
            
        prod2 = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod2
            prod2 *= nums[i]
        return res


        