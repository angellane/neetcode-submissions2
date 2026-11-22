class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0 

        res = 1
        for i in range(x):
            if i * i > x:
                return res
            res = i
        return res
        