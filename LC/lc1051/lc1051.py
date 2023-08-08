class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] - target[i]:
                res += 1
        return res