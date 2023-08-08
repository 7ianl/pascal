class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            res = 0
            while num:
                res += num%10; num//=10
            return self.addDigits(res)