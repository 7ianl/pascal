class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(p):
            res = 1
            a, b = p//n, p%n
            grid[a][b] = 0
            if a > 0 and grid[a-1][b]:
                res += dfs(p-n)
            if a < m-1 and grid[a+1][b]:
                res += dfs(p+n)
            if b > 0 and grid[a][b-1]:
                res += dfs(p-1)
            if b < n-1 and grid[a][b+1]:
                res += dfs(p+1)
            return res
        res = 0
        for i in range(m*n):
            if grid[i//n][i%n]:
                res = max(res, dfs(i))
        return res