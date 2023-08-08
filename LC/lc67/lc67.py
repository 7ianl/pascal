class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def getDecimal(x: str) -> int:
            i = len(x) -1 
            c = 0
            out = 0
            while i >= 0:
                if x[i] == '0':
                    c += 1; i -= 1
                else:
                    out += (2 ** c)
                    c += 1; i -= 1
            return out
        def getBinary(x: int) -> str:
            if x == 1:
                return str(x)
            elif x == 0:
                return '0'
            else:
                r = x % 2
                p = getBinary(x//2) + str(r)
                return p
        res = getBinary(getDecimal(a) + getDecimal(b))
        return res
                