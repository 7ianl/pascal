class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if not len(s):
            return 0
        zeroes = 0
        for i in s:
            if i == '0':
                zeroes += 1
        mem = zeroes
        for i in s:
            if i == '1':
                mem = min(mem, zeroes)
                zeroes += 1
            else:
                zeroes -= 1
                mem = min(mem, zeroes)
        return mem