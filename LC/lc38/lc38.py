class Solution:
    def countAndSay(self, n: int) -> str:
        if n > 1:
            acc = self.countAndSay(n-1)
            out = str()
            i = 0
            l = len(acc)
            while i < l:
                k = 1
                while i+k < l and acc[i+k] == acc[i]:
                    k += 1
                out += (str(k)+str(acc[i]))
                i += k
            return out
        else:
            return '1'