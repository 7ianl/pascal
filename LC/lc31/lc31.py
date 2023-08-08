class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums [i-1]:
                j = len(nums) - 1
                while nums[j] <= nums[i-1]:
                    j -= 1
                k = nums[j]
                nums[j] = nums[i-1]
                nums[i-1] = k
                nums[i:] = sorted(nums[i:])
                return
            else:
                i -= 1
        nums.sort()
        return