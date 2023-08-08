class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = {0:0, 1:1}
        if n == 0:
            return 0
        for i in range(1, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2+1]
        arr = list(dp.values())
        return max(arr)
        