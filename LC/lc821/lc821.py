class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        seen = [-100000]
        for i in range(len(s)):
            if s[i] == c:
                seen.append(i)
        j = 1
        seen.append(100000)
        res = list()
        for i in range(len(s)):
            if i > seen[j]:
                j += 1
            k = min(seen[j] - i, i - seen[j-1])
            res.append(k)
        return res