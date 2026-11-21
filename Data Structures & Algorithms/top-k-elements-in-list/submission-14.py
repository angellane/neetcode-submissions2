class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        sortedNums = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)

        return sortedNums[:k]