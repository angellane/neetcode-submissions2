class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        
            
        
        return max(hashmap, key=hashmap.get)
        