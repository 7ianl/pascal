class Solution:
    def isHappy(self, n: int) -> bool:
        def sq_sum (n):
            res = 0
            while n:
                res += (n%10) ** 2; n//=10
            return res
        seen = set()
        while True:
            n = sq_sum(n)
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)
        