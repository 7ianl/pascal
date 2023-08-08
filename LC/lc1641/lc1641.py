class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = {1:[1,1,1,1,1]}
        for i in range(2,n+1):
            dp[i] = [sum(dp[i-1][:]), sum(dp[i-1][1:]), sum(dp[i-1][2:]), sum(dp[i-1][3:]), sum(dp[i-1][4:])]
        return sum(dp[n])