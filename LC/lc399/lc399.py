class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dt, p = dict(), 0
        uf = []
        for a in equations:
            for x in a:
                if x not in dt:
                    uf.append([-1, 1])
                    dt[x] = p
                    p+=1
        cnt = [1]*len(uf)
        def pre(k):
            if uf[k][0] == -1: return [k, 1]
            else:
                x, y = pre(uf[k][0])
                uf[k][0] = x
                uf[k][1] *= y
                return uf[k]
        def join(k, m, q):
            a, b = pre(k)
            c, d = pre(m)
            if a == c: return
            if cnt[a] > cnt[c]:
                uf[c] = [a, b/(q*d)]
                cnt[a]+=cnt[c]
            else:
                uf[a] = [c, q*d/b]
                cnt[c]+=cnt[a]
        for i, (x, y) in enumerate(equations):
            join(dt[x], dt[y], values[i])
        res = []
        for x, y in queries:
            if x not in dt or y not in dt:
                res.append(-1)
                continue
            a, b = pre(dt[x])
            c, d = pre(dt[y])
            if a != c:
                res.append(-1)
                continue
            res.append(b/d)
        return res
            
        