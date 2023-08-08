class Solution:
    def numSquares(self, n: int) -> int:
        squares = set([i**2 for i in range(1, int(n**0.5)+1)])
        def dp(n, count):
            if count == 1: return n in squares
            for x in squares:
                if dp(n-x, count-1): return True
            return False
        for c in range(1, n+1):
            if dp(n, c):
                return c