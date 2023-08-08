class Solution:
    def reverseWords(self, s: str) -> str:
        s.rstrip()
        res = []
        word = ''
        for i in range(len(s)):
            if s[i] == ' ':
                if word:
                    res.append(word)
                    word = ''
            else:
                word += s[i]
        if word:
            res.append(word)
        res = reversed(res)
        return ' '.join(res)
        
        