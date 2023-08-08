class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(s)
        for t, i in enumerate(indices):
            res[i] = s[t]
        return ''.join(res)