class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        h = collections.defaultdict(list)
        s = set(range(1, n+1))
        for a, b in trust:
            h[a].append(b)
            s.discard(a)
        if len(s) != 1:
            return -1
        i = list(s)[0]
        for k, v in h.items():
            if i not in v:
                return -1
        return i
        