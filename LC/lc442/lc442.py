class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            n = abs(nums[i])-1
            if nums[n] > 0:
                nums[n] *= -1
            else:
                res.append(n+1)
        return res