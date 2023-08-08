class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start, end, mask, req = -1, -1, 0, 0
        for i in range(m*n):
            c = grid[i//n][i%n]
            if c==1:
                start = i
            elif c==2:
                end = i
            elif c==-1:
                # mark obstacles as traversed
                mask^=1<<i
            # answer requires every square traversed
            req^=1<<i
        # memoize results
        # returns number of paths from square p with traversed squares
        # set to bitmask l
        @cache
        def dp(p, l):
            # mark square traversed
            l^=1<<p
            # completion condition
            if p == end:
                if l == req:
                    return 1
                return 0
            res = 0
            # check adjacent square exists and is not traversed
            if p//n and not l&1<<(p-n):
                res += dp(p-n, l)
            if p%n and not l&1<<(p-1):
                res += dp(p-1, l)
            if p//n < m-1 and not l&1<<(p+n):
                res += dp(p+n, l)
            if p%n < n-1 and not l&1<<(p+1):
                res += dp(p+1, l)
            return res
        return dp(start, mask)
            
            