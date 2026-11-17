class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        combo = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    triplet = nums[i] + nums[k] + nums[j]
                    if triplet == 0:
                        combo = sorted(([nums[i], nums[j], nums[k]]))
                        if combo not in res:
                            res.append(combo)

        return res
                    

        #brute force solution - run time of doom and despair

        

        