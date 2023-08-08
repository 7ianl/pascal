class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1 = ''
        res2 = ''
        for x in word1:
            res1 += x
        for x in word2:
            res2 += x
        if res1 == res2:
            return True
        else:
            return False