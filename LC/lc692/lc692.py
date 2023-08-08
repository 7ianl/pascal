class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = collections.defaultdict(int)
        for w in words:
            h[w] += 1
        t = [(-y, x) for x, y in h.items()]
        print(t)
        heapq.heapify(t)
        res = []
        i = 0
        while i < k:
            w = heapq.heappop(t)
            i += 1
            acc = [w[1]]
            while (i<k and t[0][0] == w[0]):
                acc.append(heapq.heappop(t)[1])
                i += 1
            res.extend(sorted(acc))
        return res