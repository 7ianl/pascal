class Solution:
    from math import factorial
    def numTrees(self, n: int) -> int:
        return int(factorial(2*n)/(factorial(n))/(factorial(n))/(n+1))
        