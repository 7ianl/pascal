class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = set()
        g = collections.defaultdict(list)
        for x, y in prerequisites:
            if x == y: return []
            g[y].append(x)
            reqs.add(x)
        cur = set(range(numCourses)) - reqs
        red, black, L = set(), set(), list()
        def dfs(x):
            if x in red: return False
            if x in black: return True
            red.add(x)
            res = True
            for y in g[x]:
                res &= dfs(y)
            red.remove(x)
            black.add(x)
            L.append(x)
            return res
        while len(cur) != 0:
            x = list(cur)[0]
            if dfs(x) == False:
                return []
            cur -= black
        L.reverse()
        if len(L)!= numCourses: return []
        return L