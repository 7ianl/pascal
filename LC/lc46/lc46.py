class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if len(nums) == 1: return [list(nums)]
            res = []
            for x in nums:
                p = nums.copy()
                p.remove(x)
                l = helper(p)
                for i in l:
                    i.append(x)
                res.extend(l)
            return res
        return helper(list(nums))