class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2: return False
        alpha, beta = 0, 0
        nMin, nPos = 0, 0
        for i, j in zip(locked, s):
            if i == "1":
                if j == "(":
                    alpha += 1
                else:
                    alpha -= 1
            else:
                beta += 1
            if alpha + beta < 0: return False
            nMin = max(0, alpha-beta)
            nPos = max(nPos, math.ceil((nMin - alpha + beta)/2))
        return alpha - beta + 2*nPos <= 0
        