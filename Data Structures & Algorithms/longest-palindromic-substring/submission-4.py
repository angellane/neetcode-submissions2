class Solution:
    def longestPalindrome(self, s: str) -> str: #Version using a helper function to remove dead code
        resIdx = 0
        resLen = 0
        def expandFunc(l, r):
            nonlocal resIdx
            nonlocal resLen
            while l >= 0 and r < (len(s)) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expandFunc(i, i)
            expandFunc(i, i + 1)
            
        return s[resIdx : resIdx + resLen]

        