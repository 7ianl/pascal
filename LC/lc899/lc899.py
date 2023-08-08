class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        L = len(s)
        def compare(mem, i):
            for j in range(L):
                if ord(s[(mem+j)%L]) > ord(s[(i+j)%L]):
                    return False
                elif ord(s[(mem+j)%L]) < ord(s[(i+j)%L]):
                    return True
            return True
        if k != 1:
            return ''.join(sorted(list(s)))
        res = 0
        for j in range(L):
            if not compare(res, j):
                res = j
        return s[res:]+s[:res]
            