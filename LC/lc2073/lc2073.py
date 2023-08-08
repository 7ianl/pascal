class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        p = tickets[k]
        for i, j in enumerate(tickets):
            if i <= k:
                res += min(tickets[k], j)
            else:
                res += min(tickets[k]-1, j)
        return res