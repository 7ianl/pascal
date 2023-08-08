# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n+1
        while True:
            g = (low + high) // 2
            if guess(g) == 0:
                return g
            elif guess(g) == -1:
                high = g
            else:
                low = g
        
        