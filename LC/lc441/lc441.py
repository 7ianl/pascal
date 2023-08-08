class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = int((2*n)**0.5)
        return k-1 if k*(k+1) > 2*n else k