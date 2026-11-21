class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)


        temp = list(hashmap.keys())
        
        
        popper = len(temp) - k
        for i in range(popper):
            temp.remove(temp[i])

        
        return temp



        
        