class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def mapping(s):
            res = dict()
            for x in s:
                if x in res:
                    res[x] += 1
                else:
                    res[x] = 1
            return res
        return mapping(s) == mapping(t)