class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        h1 = collections.defaultdict(int)
        h2 = collections.defaultdict(int)
        for c in word1:
            h1[c]+=1
        for c in word2:
            h2[c]+=1
        for i in h1.keys():
            if abs(h1[i]-h2[i]) > 3:
                return False
        for i in h2.keys():
            if abs(h1[i]-h2[i]) > 3:
                return False
        return True