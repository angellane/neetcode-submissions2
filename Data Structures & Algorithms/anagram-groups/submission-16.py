class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #anagram has same letters and same length 

        hashmap = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in hashmap:
                hashmap[sortedS] = [s]
            else:
                hashmap[sortedS].append(s)

        return list(hashmap.values())
                

        


            


    