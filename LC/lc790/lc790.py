class Solution:
    def numTilings(self, n: int) -> int:
        dp0 = [1, 0]
        dp1 = [1, 1]
        counter, p = 1, 10**9+7
        while counter < n:
            counter += 1
            new = [(dp1[0]+dp0[0]+dp0[1]*2)%p, (dp1[0]+dp1[1])%p]
            dp0 = dp1
            dp1 = new
        return dp1[0]