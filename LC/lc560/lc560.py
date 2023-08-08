class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative = collections.defaultdict(int)
        cumulative[0] = 1
        res = 0
        s = 0
        for n in nums:
            s += n
            res += cumulative[s-k]
            cumulative[s]+=1
        return res