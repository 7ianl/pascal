class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = 1
        while abs(a**2 - num) >= 1:
            a = (a + num/a)/2
        return int(a) ** 2 == num or (int(a) + 1) ** 2 == num
            