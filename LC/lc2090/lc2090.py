class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        L, p = len(nums), k*2+1
        res = [-1]*L
        if L <= k*2: return res
        cur = sum(nums[:p])
        for i in range(p, L):
            res[i-k-1] = cur//p
            cur -= nums[i-p]
            cur += nums[i]
        res[L-k-1] = cur//p
        return res
            
            
        