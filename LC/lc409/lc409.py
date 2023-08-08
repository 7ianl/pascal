class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashed = dict()
        odds = 0
        for i in range(len(s)):
            if s[i] in hashed:
                hashed[s[i]] += 1
            else:
                hashed[s[i]] = 1
        for x in hashed.values():
            if x % 2:
                odds += 1
        if odds == 0:
            return len(s)
        else:
            return len(s) - odds + 1