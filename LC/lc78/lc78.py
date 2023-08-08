class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        L = len(nums)
        def helper(m):
            if m<0: return
            acc = []
            for k in range(L):
                if m&1<<k:
                    acc.append(nums[k])
            res.append(acc)
            return helper(m-1)
        helper(2**L - 1)
        return res