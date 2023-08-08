class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = set()
        g = collections.defaultdict(list)
        for x, y in prerequisites:
            if x == y:
                return False
            reqs.add(y)
            g[x].append(y)
        cur = set(range(numCourses)) - reqs
        if len(cur) == 0:
            return False
        seen = set()
        c = set()
        def dfs(k):
            if k in c: return False
            if k in seen: return True
            c.add(k)
            res = True
            for x in g[k]:
                res &= dfs(x)
            c.remove(k)
            seen.add(k)
            return res
        while len(cur) != 0:
            e = list(cur)[0]
            if dfs(e) == False:
                return False
            cur -= seen
        return len(set(range(numCourses)) - seen) == 0
        
            