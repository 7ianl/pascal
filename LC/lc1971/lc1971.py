class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        g = collections.defaultdict(set)
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
        seen = set()
        def helper(k):
            if k == end: return True
            seen.add(k)
            for n in g[k]:
                if n not in seen and helper(n):
                    return True
            return False
        return helper(start)