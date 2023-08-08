class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        h = dict()
        for p, b in items:
            if b not in h:
                h[b] = p
            else:
                h[b] = min(h[b], p)
        l = list(map(list, list(h.items())))
        l.sort(key =lambda x: x[0], reverse = True)
        cur_min = l[0][1]
        for i in range(1, len(l)):
            cur_min = min(cur_min, l[i][1])
            l[i][1] = cur_min
        l.reverse()
        prices = [x[1] for x in l]
        l = [x[0] for x in l]
        res = []
        for x in queries:
            c = bisect.bisect_right(prices, x) -1
            if c < 0:
                res.append(0)
            else:
                res.append(l[c])
        return res