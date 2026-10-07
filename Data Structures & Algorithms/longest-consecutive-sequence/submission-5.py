class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        memo = {}

        def dfs(n):
            if n not in numSet:
                return 0
            if n in memo:
                return memo[n]

            memo[n] = 1 + dfs(n + 1)
            return memo[n]
            
        longest = 0
        for n in numSet:
            longest = max(longest, dfs(n))
        return longest
            

        