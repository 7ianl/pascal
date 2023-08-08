class Solution:
    def partition(self, s: str) -> List[List[str]]:
        L, h = len(s), list(s)
        def paChecker(start, end):
            lo, hi = start, end
            while lo < hi:
                if h[lo] != h[hi]:
                    return False
                lo += 1
                hi -= 1
            return True
        @cache
        def partitionAux(n):
            if n == L: return [[]]
            ret = []
            for i in range(n, L):
                if paChecker(n, i):
                    acc = s[n:i+1]
                    cur = partitionAux(i+1)
                    for t in cur:
                        p = t[:]
                        p.append(acc)
                        ret.append(p)
            return ret
        return [list(reversed(n)) for n in partitionAux(0)]
                    
    