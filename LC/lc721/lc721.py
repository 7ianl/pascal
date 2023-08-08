class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        h, h1 = dict(), dict()
        assoc = dict()
        for entry in accounts:
            name = entry[0]
            for i in range(1, len(entry)):
                if entry[i] not in h:
                    h1[len(h)] = entry[i]
                    assoc[len(h)] = name
                    h[entry[i]] = len(h)
        prev = [-1]*len(h)
        sizes = [1]*len(h)
        def find(k):
            if prev[k] == -1: return k
            prev[k] = find(prev[k])
            return prev[k]
        def join(a, b):
            a, b = find(a), find(b)
            if a == b: return
            if sizes[a] > sizes[b]:
                a, b = b, a
            prev[a] = b
            sizes[b] += sizes[a]
            return
        for entry in accounts:
            a = h[entry[1]]
            for i in range(2, len(entry)):
                join(a, h[entry[i]])
        t = collections.defaultdict(list)
        for i in range(len(prev)):
            t[find(i)].append(h1[i])
        return [[assoc[x], *sorted(y)] for x, y in t.items()]