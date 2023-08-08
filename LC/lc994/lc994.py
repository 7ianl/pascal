class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def inGrid(r, c):
            return r >= 0 and r < m and c >= 0 and c < n
        def validNxt(r, c):
            res = []
            a1, a2 = [r-1, r+1, r, r], [c, c, c-1, c+1]
            for x, y in zip(a1, a2):
                if inGrid(x, y) and grid[x][y] == 1:
                    res.append((x, y))
            return res
        def bfs(cur):
            nxt = []
            for r, c in cur:
                for x, y in validNxt(r, c):
                    grid[x][y] = grid[r][c]+1
                    nxt.append((x, y))
            if len(nxt) == 0: return
            return bfs(nxt)
        init = []
        for i in range(m*n):
            if grid[i//n][i%n] == 2:
                init.append((i//n, i%n))
        bfs(init)
        res = 0
        for i in range(m*n):
            if grid[i//n][i%n] == 1:
                return -1
            res = max(res, grid[i//n][i%n])
        if res == 0: return 0
        return res -2