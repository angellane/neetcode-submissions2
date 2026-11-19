class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 1
        curr = []
        res = 0
        while r < len(s):
            while s[r] in curr:
                curr.pop(0)
                l += 1
            curr.append(s[r])
            res = max(len(curr), res)
            r+=1
        return res



        