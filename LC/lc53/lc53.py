class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCont, maxSoFar = -1000000, -1000000
        for c in nums:
            maxCont = max(c, maxCont + c)
            maxSoFar = max(maxCont, maxSoFar)
        return maxSoFar