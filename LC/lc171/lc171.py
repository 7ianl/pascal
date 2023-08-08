class Solution:
    def titleToNumber(self, s: str) -> int:
        multiplier = 1
        res = 0
        while s:
            k = ord(s[-1]) - ord('A') + 1
            res += k * multiplier
            multiplier *= 26
            s = s[:-1]
        return res
        