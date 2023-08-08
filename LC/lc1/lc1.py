class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for i in range(len(nums)):
            c = nums[i]
            b = target - c
            if b in hashed:
                return [i, hashed[b]]
            hashed[c] = i
        return [0, 0]