from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        L = len(endWord)
        combos = defaultdict(list)
        for word in wordList:
            for i in range(L):
                combos[word[:i]+'*'+word[i+1:]].append(word)
        queue = collections.deque([(beginWord,1)])
        visited = {beginWord}
        while queue:
            current, l = queue.popleft()
            for i in range(L):
                intermediate = current[:i] +'*'+current[i+1:]
                for word in combos[intermediate]:
                    if word == endWord:
                        return l+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word,l+1))
                combos[intermediate] = []
        return 0
        