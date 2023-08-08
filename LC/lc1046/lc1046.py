class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        while len(stones)>1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, a-b)
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]