class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) < 3:
            return max(s)
        return sorted(list(s))[-3]
        