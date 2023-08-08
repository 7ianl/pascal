class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if not nums[i]:
                continue
            nums[p] = nums[i]
            if i > p:
                nums[i] = 0
            p += 1
            