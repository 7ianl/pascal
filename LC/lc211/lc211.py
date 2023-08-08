Trie = lambda: collections.defaultdict(Trie)
from functools import reduce
END = True
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        reduce(dict.__getitem__, word, self.root)[END] = True

    def search(self, word: str) -> bool:
        def helper(t, w):
            if w == '': return t.get(END, False)
            n = w[1:]
            if w[0] == '.':
                res = False
                for i in t.keys():
                    if i != END:
                        res |= helper(t[i], n)
                return res
            else:
                if w[0] not in t: return False
                return helper(t[w[0]], n)
        return helper(self.root, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)