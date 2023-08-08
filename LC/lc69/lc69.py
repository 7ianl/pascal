class Solution:
    def mySqrt(self, x: int) -> int:
        res = 1
        while abs(res **2 - x) >= 1:
            res = (res + x/res)/2
        return int(res)
        