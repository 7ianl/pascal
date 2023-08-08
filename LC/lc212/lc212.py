from functools import reduce
Trie = lambda: collections.defaultdict(Trie)
END = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            reduce(dict.__getitem__, word, trie)[END] = True
        m, n = len(board), len(board[0])

        def deleteWord(w): reduce(dict.__getitem__, w, trie)[END] = False
            
        def search(p):
            #seen = set()
            acc = []
            def dfs(k, w, t):
                #if k in seen: return
                #seen.add(k)
                c = board[k//n][k%n]
                
                if c not in t: return
                t, w = t[c], w+c
                if t.get(END, False): 
                    acc.append(w)
                    deleteWord(w)
                board[k//n][k%n] = '#'
                if k%n > 0:
                    dfs(k-1, w, t)
                if k%n < n-1:
                    dfs(k+1, w, t)
                if k//n > 0:
                    dfs(k-n, w, t)
                if k//n < m-1:
                    dfs(k+n, w, t)
                #seen.remove(k)
                board[k//n][k%n] = c
                return
            dfs(p, '', trie)
            return acc
        
        res = []
        for i in range(m*n):
            res.extend(search(i))
        return res
                    