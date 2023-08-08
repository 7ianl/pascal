class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c1, c2, p1, p2 = 10**6, 10**6, 0, 0
        for p in prices:
            c1 = min(c1, p)
            p1 = max(p1, p-c1)
            c2 = min(c2, p-p1)
            p2 = max(p2, p-c2)
        return p2