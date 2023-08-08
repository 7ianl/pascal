class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-k % len(nums)):
            n = nums.pop(0)
            nums.append(n)