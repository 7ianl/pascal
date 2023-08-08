class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def bitmask(w):
            out = 0
            for x in w:
                out |= 1<<(ord(x)-97)
            return out
        wordsCount = collections.Counter(bitmask(w) for w in words)
        res = []
        for p in puzzles:
            m1 = 1<<(ord(p[0])-97)
            acc = wordsCount[m1]
            m2 = bitmask(p[1:])
            submask = m2
            while submask:
                acc += wordsCount[submask|m1]
                submask = (submask-1)&m2
            res.append(acc)
        return res
                