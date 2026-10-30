class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tchars= []
        l, r = 0, 1
        
        for c in t:
            tchars.append(c)

        while l < r:
            l = s.find(t)
            r = l + 1
            for i in range(s.find(t), len(s) - 1):
                r = len(s) - 1
                if s[r] in tchars:
                    res = s[l : r + 1]

        return res


        