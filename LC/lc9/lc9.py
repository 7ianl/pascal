class Solution:
    def isPalindrome(self, x: int) -> bool:
        def numDigits(x):
            for i in range(12):
                if 10 ** i > x:
                    return i
            return 0
        def NthDigit(x: int, n: int):
            for i in range (n-1):
                x //= 10
            return x % 10
        if x < 0:
            return False
        if x == 0:
            return True
        else:
            k = numDigits(x)
            for i in range(k//2):
                if NthDigit(x, 1+i) != NthDigit(x, k-i):
                    return False
            return True