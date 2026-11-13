class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0 
        profit = 0
        res = 0
        currMin = prices[0]
        while r < len(prices) and l < r:
            currMin = min(currMin, prices[r])

            currProfit = prices[r] - currMin 
            r += 1
            
            profit = max(currProfit, profit)

        return profit 
        