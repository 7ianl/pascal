class Union:
    def __init__(self, n):
        self.parents = [-1]*n
        self.ranks = [1]*n
    def find(self, k):
        if self.parents[k] == -1: return k
        self.parents[k] = self.find(self.parents[k])
        return self.parents[k]
    def join(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return
        if self.ranks[a] >= self.ranks[b]:
            a, b = b, a
        self.parents[a] = b
        self.ranks[b] += self.ranks[a]
class Factorize:
    def __init__(self, n):
        self.spf = [i for i in range(n)]
        self.n = n
        self.sieve()
    def sieve(self):
        for i in range(2, int(self.n**0.5)+1):
            if self.spf[i] == i:
                for j in range(i*i, self.n, i):
                    if self.spf[j] == j:
                        self.spf[j] = i
    def getPrimes(self, k):
        res = []
        while k > 1:
            p = self.spf[k]
            res.append(p)
            while k % p == 0:
                k //= p
        return res

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        m_num = max(nums)
        mp = defaultdict(list)
        dsu = Union(len(nums))
        factorizer = Factorize(m_num+1)
        for i, k in enumerate(nums):
            for p in factorizer.getPrimes(k):
                mp[p].append(i)
        for p in mp:
            for i in range(1, len(mp[p])):
                dsu.join(mp[p][i], mp[p][i-1])
        return max(dsu.ranks)
        