from functools import reduce
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        Trie = lambda: collections.defaultdict(Trie)
        t = Trie()
        END = True
        res = []
        for w in dictionary:
            reduce(dict.__getitem__, w, t)[END] = w
        def search(word):
            h = t
            for c in word:
                if c not in h or END in h: break
                h = h[c]
            return h.get(END, word)
        return ' '.join(map(search, sentence.split()))