class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        n = len(jobDifficulty)
        dp = [float("inf")] * (n + 1)
        dp[n] = 0

        for day in range(1, d + 1):
            for i in range(n - day + 1):
                maxi = 0
                dp[i] = float("inf")
                for j in range(i, n - day + 1):
                    maxi = max(maxi, jobDifficulty[j])
                    dp[i] = min(dp[i], maxi + dp[j + 1])

        return dp[0]