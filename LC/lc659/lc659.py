class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        p, q, cur = 0, 0, []
        while p < len(nums):
            n = nums[p]
            if n > q+1:
                if 1 in cur or 2 in cur:
                    return False
                cur = []
            nxt, q = [], n
            while p < len(nums) and nums[p] == n:
                if len(cur) == 0:
                    heapq.heappush(nxt, 1)
                else:
                    heapq.heappush(nxt, 1+heapq.heappop(cur))
                p+=1
            if 1 in cur or 2 in cur:
                return False
            cur = nxt
        return not(1 in cur or 2 in cur)
                