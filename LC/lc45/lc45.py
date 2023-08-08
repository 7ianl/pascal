class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX_NUM = 100000
        L = len(nums)
        res = [MAX_NUM]*(L-1)
        res.append(0)
        for i in range(L-2, -1, -1):
            for j in range(i+1, min(L, i+nums[i]+1)):
                res[i] = min(res[i], res[j]+1)
        return res[0]