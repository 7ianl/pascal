class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dset = [-1]*n
        rank = [0]*n
        def find(p):
            if dset[p]==-1: return p
            dset[p] = find(dset[p])
            return dset[p]
        def join(a, b):
            c, d = find(a), find(b)
            if c == d: return True
            if d in h[c] or c in h[d]: return False
            if rank[c] < rank[d]:
                dset[c] = d
                h[d].update(h[c])
                for x in h[d]:
                    h[x].add(d)
            elif rank[c] > rank[d]:
                dset[d] = c
                h[c].update(h[d])
                for x in h[c]:
                    h[x].add(c)
            else:
                dset[d] = c
                h[c].update(h[d])
                for x in h[c]:
                    h[x].add(c)
                rank[c]+=1
            return True
        h = collections.defaultdict(set)
        for x, y in restrictions:
            h[x].add(y)
            h[y].add(x)
        res = []
        for x, y in requests:
            res.append(join(x, y))
        return res