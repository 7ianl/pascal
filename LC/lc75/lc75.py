class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, len(nums)
        for x in nums:
            if x == 0:
                p1+=1
            elif x == 2:
                p2 -= 1
        for i in range(p1):
            nums[i] = 0
        for i in range(p1, p2):
            nums[i]=1
        for i in range(p2, len(nums)):
            nums[i]=2