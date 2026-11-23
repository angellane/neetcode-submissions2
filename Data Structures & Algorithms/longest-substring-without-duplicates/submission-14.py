class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()

        l, r = 0, 1
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            res = max(len(seen), res)
        return res
            
                
                


            
            
        