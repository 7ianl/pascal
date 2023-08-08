class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = dict()
        for i in range(len(points)):
            h[i] = points[i][0]**2 + points[i][1]**2
        seq = [(y, x) for x, y in h.items()]
        heapq.heapify(seq)
        res = []
        for i in range(k):
            res.append(points[heapq.heappop(seq)[1]])
        return res