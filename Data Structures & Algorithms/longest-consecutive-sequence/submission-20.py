class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 
        if not nums:
            return 0
        res = 1
        #sortNums = sorted(nums)
        nums.sort()
        count = 1

        for i in range(len(nums) - 1, 0, -1):
            curr = nums[i]
            next = nums[i - 1]
            
            if curr - next == 1:
                count+=1
                res = max(res, count)
            elif curr == next:
                continue
            else:
                count = 1

        
        return res
        #passes 2 test cases but doesnt account for 
            
            
                
        