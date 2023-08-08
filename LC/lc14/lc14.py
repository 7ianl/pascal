class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        l = len(strs)
        if strs == []:
            return ''
        Max = len(strs[0])
        if strs[0] == '':
            return ''
        for x in strs:
            Max = min(Max, len(x))
        while i < Max:
            for x in range(l):
                val = strs[0][i]
                if strs[x][i] != val:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]