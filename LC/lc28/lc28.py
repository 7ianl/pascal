class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        i = 0
        n = len(needle)
        N = len(haystack) - n
        while i <= N:
            if haystack[i:i+n] == needle:
                return i
            i += 1
        return -1