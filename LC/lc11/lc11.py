class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, i = 0, 0
        r, j = len(height) - 1, len(height) - 1
        v = min(height[l], height[r]) * (r - l)
        while i < j:
            if height[l] < height[r]:
                while i < r:
                    i += 1
                    if height[i] <= height[l]:
                        continue
                    else:
                        vp = min(height[i], height[r]) * (r - i)
                        v, l = max(v,vp), i
                        break
            else:
                while l < j:
                    j -= 1
                    if height[j] <= height[r]:
                        continue
                    else:
                        vp = min(height[l], height[j]) * (j - l)
                        v, r = max(v,vp), j
                        break
        return v