class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def counts(word):
            res = dict()
            for i in range(len(word)):
                if word[i] in res:
                    res[word[i]] += 1
                else:
                    res[word[i]] = 1
            return res
        x = counts(word1)
        y = counts(word2)
        x1 = set(x.keys()); x2 = set(x.values()); y1 = set(y.keys()); y2 = set(y.values())
        return x1 == y1 and x2 == y2