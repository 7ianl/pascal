class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def getNum(m, n):
            return grid[-m][-n]
        ans = dict()
        ans[(1, 1)] = getNum(1, 1)
        m = len(grid)
        n = len(grid[0])
        for i in range(2, m+1):
            ans[(i, 1)] = getNum(i, 1) + ans[(i-1, 1)]
        for i in range(2, n+1):
            ans[(1, i)] = getNum(1, i) + ans[(1, i-1)]
        for i in range(2, m+1):
            for j in range(2, n+1):
                ans[(i, j)] = getNum(i, j) + min(ans[(i-1, j)], ans[(i, j-1)])
        return ans[(m, n)]
        