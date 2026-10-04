class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s)) #sorted returns the sorted elements as a new list 
            res[sortedS].append(s)

        return list(res.values())


            


    