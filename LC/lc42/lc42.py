class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        p = height.index(max(height))
        hedge = 0
        res = 0
        for i in range(p):
            if height[i] < hedge:
                res += (hedge - height[i])
            else:
                hedge = height[i]
        hedge = 0
        for j in range(len(height)-1, p, -1):
            if height[j] < hedge:
                res += (hedge - height[j])
            else:
                hedge = height[j]
        return res