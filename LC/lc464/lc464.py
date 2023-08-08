class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal > maxChoosableInteger**2: return False
        @cache
        def dp(m, r):
            if r <= maxChoosableInteger:
                if r == 0: return True
                for i in range(r, maxChoosableInteger+1):
                    if not m&1<<(i-1):
                        return True
            a = False
            for i in range(1, maxChoosableInteger+1):
                if not m&1<<(i-1):
                    a = a or not dp(m^1<<(i-1), r-i)
            return a
        return dp(0, desiredTotal)