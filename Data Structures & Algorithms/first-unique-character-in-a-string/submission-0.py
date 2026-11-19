class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()

        for i, n in enumerate(s):
            if n in s:
                continue
            else:
                return i
            s.add(c)
        return -1
            
        