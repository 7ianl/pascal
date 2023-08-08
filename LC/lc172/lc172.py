class Solution:
    def trailingZeroes(self, n: int) -> int:
        t = 0
        n //= 5
        while n:
            t += n
            n //= 5
        return t