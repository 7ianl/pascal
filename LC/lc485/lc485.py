class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        out = 0
        for x in nums:
            if x:
                res += 1
            elif res:
                out = max(out, res)
                res = 0
        return max(out,res)
        