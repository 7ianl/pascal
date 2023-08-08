class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        rec = dict()
        if len(words) != len(pattern):
            return False
        r = []
        for i in range(len(pattern)):
            r.append(pattern[i])
        if len(set(r)) != len(set(words)):
            return False
        for i in range(len(words)):
            if pattern[i] in rec:
                if rec[pattern[i]] != words[i]:
                    return False
            else:
                rec[pattern[i]] = words[i]
        return True