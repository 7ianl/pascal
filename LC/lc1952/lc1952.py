class Solution:
    def isThree(self, n: int) -> bool:
        t = math.floor(math.sqrt(n))
        if t == 1:
            return False
        if t * t != n:
            return False
        else:
            for i in range(2, math.floor(math.sqrt(t))+1):
                if t%i == 0 and t != i:
                    return False
            return True