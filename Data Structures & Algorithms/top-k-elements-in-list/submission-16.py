class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)


        temp = list(hashmap.keys())
        
        popper = len(temp) - k
        for i in range(popper):
            leastFreq = min(hashmap, key = hashmap.get)
            temp.remove(leastFreq)
            hashmap.pop(leastFreq)

        
        return temp



        
        