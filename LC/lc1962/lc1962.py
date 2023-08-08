class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        def myfunc(x): return -x
        piles = list(map(myfunc, piles))
        heapq.heapify(piles)
        def helper(piles, iteration):
            if iteration >= k:
                return
            else:
                p = heapq.heappop(piles)
                p = -(-p - (-p//2))
                heapq.heappush(piles, p)
                return helper(piles, iteration+1)
        helper(piles, 0)
        return -sum(piles)
                