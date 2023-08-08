class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortWord(w):
            return ''.join(sorted(list(w)))
        hashed = {}
        for s in strs:
            h = sortWord(s)
            if h in hashed:
                hashed[h].append(s)
            else:
                hashed[h] = [s]
        return list(hashed.values())