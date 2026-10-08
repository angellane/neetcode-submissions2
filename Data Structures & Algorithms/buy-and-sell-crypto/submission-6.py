class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                res = max(res, curr) #all this checks to see if we have a new max price
            else:
                l = r #if l becomes greater or equal to r then l becomes r and r is incremented this is the sliding part of sliding window
            r+=1 
        return res


        