class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y:
            return 0
        if x% 2 == y %2: 
            return self.hammingDistance(x>>1, y>>1)
        return 1+ self.hammingDistance(x>>1, y>>1)