class Trie:

    def __init__(self):
        self.root = collections.defaultdict(str)

    def insert(self, word: str) -> None:
        h = self.root
        for c in word:
            if c not in h:
                h[c] = collections.defaultdict(str)
            h = h[c]
        h["_end"] = True

    def search(self, word: str) -> bool:
        h = self.root
        for c in word:
            if c not in h:
                return False
            h = h[c]
        return h["_end"] == True
        

    def startsWith(self, prefix: str) -> bool:
        h = self.root
        for c in prefix:
            if c not in h:
                return False
            h = h[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)