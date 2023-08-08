class DSU:
    def __init__(self, n):
        self.prevs = [-1]*n
        self.sizes = [1]*n
    def find(self, k):
        if self.prevs[k] == -1: return k
        self.prevs[k] = self.find(self.prevs[k])
        return self.prevs[k]
    def join(self, a, b):
        p, q = self.find(a), self.find(b)
        if p == q: return
        if self.sizes[p] < self.sizes[q]:
            p, q = q, p
        self.prevs[q] = p
        self.sizes[p] += self.sizes[q]
        return

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        h = collections.defaultdict(set)
        m = collections.defaultdict(list)
        for a, b, t in meetings:
            h[t].add(a)
            h[t].add(b)
            m[t].append((a, b))
        dsu = DSU(n)
        dsu.join(0, firstPerson)
        ret = set()
        for x in sorted(list(h.keys())):
            p = dsu.find(0)
            persons = list(h[x])
            hash_persons1 = {y: x for x, y in enumerate(persons)}
            hash_persons2 = {x: y for x, y in enumerate(persons)}
            info = DSU(len(persons))
            for a, b in m[x]:
                info.join(hash_persons1[a], hash_persons1[b])
            insiders = set()
            for person in persons:
                if dsu.find(person) == p:
                    insiders.add(person)
            insiders = set([info.find(hash_persons1[person]) for person in insiders])
            for x in range(len(persons)):
                if info.find(x) in insiders:
                    dsu.join(0, hash_persons2[x])
        p = dsu.find(0)
        return [i for i in range(n) if dsu.find(i) == p]
        
        
        
        