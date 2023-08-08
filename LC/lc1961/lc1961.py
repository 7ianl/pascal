class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        def helper(s, wordlst):
            if s == '':
                return True
            elif len(wordlst) == 0:
                return False
            else:
                w = wordlst.pop(0)
                l1 = len(s)
                l2 = len(w)
                if l1 < l2:
                    return False
                elif w == s[:l2]:
                    return helper(s[l2:], wordlst)
                else:
                    return False
        return helper(s, words)