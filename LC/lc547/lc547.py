class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dset, rank = [-1]*n, [1]*n
        self.size = n
        def find(k):
            if dset[k]==-1: return k
            dset[k] = find(dset[k])
            return dset[k]
        def join(a, b):
            c, d = find(a), find(b)
            if c == d: return
            self.size -= 1
            if rank[c] < rank[d]:
                dset[c] = d
            elif rank[c] > rank[d]:
                dset[d] = c
            else:
                rank[c] += 1
                dset[d] = c
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    join(i, j)
        return self.size