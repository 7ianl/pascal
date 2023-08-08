class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        positions= set()
        for x in pairs:
            for y in x:
                positions.add(y)

        n = len(positions)
        #self.groups = n
        dset = [-1]*n
        rank = [0]*n
        def find(x):
            if dset[x] == -1: return x
            dset[x] = find(dset[x])
            return dset[x]
        def join(a, b):
            c, d = find(a), find(b)
            if c==d: return
            #self.groups -= 1
            if rank[c]<rank[d]:
                dset[c] = d
            elif rank[c]>rank[d]:
                dset[d] = c
            else:
                rank[c]+=1
                dset[d]=c
        l = list(positions)
        l.sort()
        i = 0
        hpos1, hpos2 = dict(), dict()
        for x in l:
            hpos1[x] = i
            hpos2[i] = x
            i +=1
        for x, y in pairs:
            join(hpos1[x], hpos1[y])
        arrangements = collections.defaultdict(list)
        for i in range(n):
            arrangements[find(i)].append(hpos2[i])
        S = [x for x in s]
        for l1 in arrangements.values():
            l2 = [S[x] for x in l1]
            l2.sort()
            for i, x in enumerate(l1):
                S[x] = l2[i]
        return ''.join(S)
                
        
            