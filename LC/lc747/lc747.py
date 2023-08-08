class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        p1, p2 = (-1, -1), (-1, -1)
        for i, x in enumerate(nums):
            if x > p2[0]:
                p2 = (x, i)
                if p2[0] > p1[0]:
                    p1, p2 = p2, p1
        if p1[0] >= p2[0]*2: return p1[1]
        return -1