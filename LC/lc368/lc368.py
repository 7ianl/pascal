class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = dict()
        dp[-1] = set()
        nums.sort()
        for n in nums:
            acc = set()
            for s in dp.keys():
                if n%s == 0 and len(dp[s]) > len(acc):
                    acc = dp[s].copy()
            acc.add(n)
            dp[n] = acc

        res = max(dp.values(), key = len)
        return list(res)