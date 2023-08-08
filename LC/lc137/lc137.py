class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = sum(set(nums))
        allSum = sum(nums)
        return (once * 3 - allSum)//2
        