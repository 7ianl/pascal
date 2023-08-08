class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        res = [1, 0]
        for _ in range(n-1):
            t = res[0]
            res[0] += res[1]
            res[1] = t
        return res[0]