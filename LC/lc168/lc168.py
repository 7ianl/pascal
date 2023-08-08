class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            k = n % 26
            if k == 0:
                k = 26
            add = chr(k+64)
            res = add + res
            n = (n-1) // 26
        return res