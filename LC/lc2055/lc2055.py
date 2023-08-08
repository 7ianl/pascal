class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pSum = [0]*len(s)
        pSum[0] = int(s[0] == '*')
        for i in range(1, len(s)):
            pSum[i] = int(s[i] =='*') + pSum[i-1]
        cAft = [-1]*len(s)
        cBef = [-1]*len(s)
        if s[0]=='|':
            cBef[0] = 0
        for i in range(1, len(s)):
            if s[i] == '|':
                cBef[i] = i
            else:
                cBef[i] =cBef[i-1]
        if s[-1] =='|':
            cAft[-1] = len(s)-1
        for i in range(len(s)-2, -1, -1):
            if s[i]=='|':
                cAft[i] = i
            else:
                cAft[i] =cAft[i+1]
        def helper(a, b):
            if cAft[a] == -1 or cBef[b] == -1 or cAft[a] >= cBef[b]:
                return 0
            else:
                return pSum[cBef[b]]-pSum[cAft[a]]
        res = []
        print(pSum)
        for x, y in queries:
            res.append(helper(x, y))
        return res
                