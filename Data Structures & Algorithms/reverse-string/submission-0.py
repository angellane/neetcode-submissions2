class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        while l < r:
            if ord(s[l]) < ord(s[r]):
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l+=1
            elif ord(s[l]) > ord(s[r]):
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                r-=1
            l+=1
            r-=1
                
        

        