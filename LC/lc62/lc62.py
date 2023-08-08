class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(a, b):
            if a <= 1 or b<= 1: return 1
            return helper(a-1, b) + helper(a, b-1)
        return helper(m, n)