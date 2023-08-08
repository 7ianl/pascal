class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(m, p):
            if p == 0: return 1
            s = 0
            for i in range(n):
                if not m & (1 << i) and ((i+1)%p == 0 or p%(i+1) == 0):
                    s += dfs(m ^ (1 << i), p-1)
            return s
        return dfs(0, n)