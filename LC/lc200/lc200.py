class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def loc(p):
            res = []
            if p//n != 0:
                res.append(p-n)
            if p//n != m-1:
                res.append(p+n)
            if p%n != 0:
                res.append(p-1)
            if p%n != n-1:
                res.append(p+1)
            return res
        def bfs(cur):
            nxt = []
            for p in cur:
                for x in loc(p):
                    if grid[x//n][x%n] == '1':
                        grid[x//n][x%n] = '3'
                        nxt.append(x)
            if len(nxt)==0: return
            return bfs(nxt)
        num = 0
        for i in range(m*n):
            if grid[i//n][i%n] == '1':
                grid[i//n][i%n] = '3'
                bfs([i])
                num += 1
        return num