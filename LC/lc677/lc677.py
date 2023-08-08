class MapSum:

    def __init__(self):
        self.root = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        h = self.root
        for c in key:
            if c not in h:
                h[c] = collections.defaultdict(int)
            h = h[c]
        h['_val'] = val
            

    def sum(self, prefix: str) -> int:
        def dfs(t):
            if type(t) == int: return t
            res = 0
            for i in t.values():
                res += dfs(i)
            return res
        h = self.root
        for c in prefix:
            if c not in h:
                return 0
            h = h[c]
        return dfs(h)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)