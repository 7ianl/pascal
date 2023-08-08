class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(set)
        res = [0]*n
        count = [1]*n
        for i, j in edges:
            g[i].add(j)
            g[j].add(i)
        
        def dfs1(root, pre):
            for i in g[root]:
                if i != pre:
                    dfs1(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        def dfs2(root, pre):
            for i in g[root]:
                if i != pre:
                    res[i] = res[root] -2*count[i] + n
                    dfs2(i, root)
        dfs1(0, -1)
        dfs2(0, -1)
        return res