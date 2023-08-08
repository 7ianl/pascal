class Solution:
    def countVowels(self, word: str) -> int:
        counts = [0]
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for x in word:
            if x in vowels:
                counts.append(counts[-1]+1)
            else:
                counts.append(counts[-1])
        prefix = counts[:]
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        L, N = len(prefix), prefix[-1]
        res = 0
        for i in range(L):
            res += (N-prefix[i]-counts[i]*(L-i-1))
        return res