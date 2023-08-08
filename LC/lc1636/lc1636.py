class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        h = collections.defaultdict(int)
        for x in nums:
            h[x] +=1
        t = [(y, x) for x, y in h.items()]
        heapq.heapify(t)
        res = []
        while t:
            k = t[0][0]
            q = []
            while t and t[0][0]==k:
                q.append(heapq.heappop(t)[1])
            q.sort(reverse=True)
            for i in q:
                res += [i]*k
        return res