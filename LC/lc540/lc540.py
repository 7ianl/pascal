class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return functools.reduce(operator.xor, nums, 0)