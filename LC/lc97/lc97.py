class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        @cache
        def dp(a, b):
            if a == b and a == -1: return True
            if a == -1:
                if s3[b] != s2[b]: return False
                return dp(a, b-1)
            if b == -1:
                if s3[a] != s1[a]: return False
                return dp(a-1, b)
            if s3[a+b+1] == s1[a]:
                if s3[a+b+1] == s2[b]:
                    return dp(a, b-1) or dp(a-1, b)
                return dp(a-1, b)
            if s3[a+b+1] == s2[b]:
                return dp(a, b-1)
            return False
        return dp(len(s1)-1, len(s2)-1)