class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        l = len(dp)
        while l > 1:
            l -= 1
            arr = triangle[l-1]
            for i in range(l):
                dp[i] = min(dp[i] + arr[i], dp[i+1] + arr[i])
        return dp[0]
        