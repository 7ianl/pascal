class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = collections.defaultdict(int)
        for x in nums:
            h[x] += 1
        t = [(-y, x) for x, y in h.items()]
        heapq.heapify(t)
        res = []
        for i in range(k):
            res.append(heapq.heappop(t)[1])
        return res