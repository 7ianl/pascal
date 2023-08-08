class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        cur = 0
        for i in range(len(nums)):
            if cur * 2 == S-nums[i]:
                return i
            cur += nums[i]
        return -1