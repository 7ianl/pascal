class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        S = sum(nums)
        nums.sort(reverse=True)
        if S%k != 0: return False
        p = S//k
        @lru_cache(None)
        def dfs(m, r, t):
            if r == 0:
                return True
            if t == 0:
                return dfs(m, r, p)
            for i in range(N):
                if not m&(1<<i) and nums[i]<=t:
                    if dfs(m^(1<<i), r-1, t-nums[i]):
                        return True
            return False          
        return dfs(0, N, p)