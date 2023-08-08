class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        C, P = [10000]*k, [0]*(k+1)
        for p in prices:
            for i in range(k):
                C[i] = min(C[i], p-P[i])
                P[i+1] = max(P[i+1], p-C[i])
        return P[k]