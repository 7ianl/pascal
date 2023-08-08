class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(string):
            res = ''
            for c in string:
                res += str(ord(c)-96)
            return res
        def oper(string):
            res = 0
            for c in string:
                res += int(c)
            return str(res)
        p = transform(s)
        for i in range(k):
            p = oper(p)
        return int(p)
        