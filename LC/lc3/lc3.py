class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        LongestSoFar = 0
        LongestCont = 0
        charsSoFar = dict()
        for i in range(len(s)):
            if s[i] in charsSoFar:
                LongestCont = min(LongestCont + 1, i - charsSoFar[s[i]])
                LongestSoFar = max(LongestSoFar, LongestCont)
                charsSoFar[s[i]] = i
            else:
                LongestCont += 1
                LongestSoFar = max(LongestSoFar, LongestCont)
                charsSoFar[s[i]] = i
        return LongestSoFar
        