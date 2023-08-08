class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        res = [1]*L
        prod = 1
        for i in range(1, L):
            prod *= nums[i-1]
            res[i] *= prod
        prod = 1
        for i in range(L-1, 0, -1):
            prod *= nums[i]
            res[i-1] *= prod
        return res
        