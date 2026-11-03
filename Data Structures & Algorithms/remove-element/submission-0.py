class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = [] * len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                temp.append(nums.pop(i))
            else:
                i+=1
                


        k = len(nums)
        nums += temp

        return k


            


            
        