class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        index = dict()
        for x in nums:
            if x not in index:
                index[x] = 1
            else:
                index[x] += 1
        res = 0
        for x,y in index.items():
            if k-x in index:
                res += min(y, index[k-x])
        return res//2