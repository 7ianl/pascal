class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': continue
                dp[i][j] = dp[i][j-1] + 1 if j else 1
                maxWidth = dp[i][j]
                for k in range(i, -1, -1):
                    maxWidth = min(maxWidth, dp[k][j])
                    maxArea = max(maxArea, maxWidth*(i-k+1))
            
        return maxArea