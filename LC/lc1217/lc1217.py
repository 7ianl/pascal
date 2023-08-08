class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        c1, c2 = 0, 0
        for v in position:
            if v%2:
                c2 += 1
            else:
                c1 += 1
        return min(c1, c2)