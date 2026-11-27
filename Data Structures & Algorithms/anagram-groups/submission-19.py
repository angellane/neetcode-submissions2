class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedS = []
        sortToOrig = {}
        for word in strs:
            sortedS.append(''.join(sorted(word)))
        
        for i in range(len(strs)):
            if sortedS[i] not in sortToOrig:
                sortToOrig[sortedS[i]] = []
            sortToOrig[sortedS[i]].append(strs[i])


        return list(sortToOrig.values())
        