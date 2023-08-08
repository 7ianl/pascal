class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            if not len(str(x)) % 2:
                res += 1
        return res
        