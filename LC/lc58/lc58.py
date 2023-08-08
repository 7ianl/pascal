class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        i = len(s) - 1
        while s[i] == ' ' and i >= 0:
            i -= 1
        while s[i] != ' ' and i >= 0:
            out += 1
            i -= 1
        return out