from heapq import heapify, heappop
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        heapify(nums)
        cur, acc, res = heappop(nums), 1, 1
        while nums:
            nxt = heappop(nums)
            if nxt == cur: continue
            if nxt == cur +1:
                acc += 1
            else:
                res = max(res, acc)
                acc = 1
            cur = nxt
        return max(res, acc)