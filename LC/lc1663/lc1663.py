class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        p = k - n
        q = p % 25
        num_z = p // 25
        if q:
            b = 1
        else:
            b = 0
        num_a = n - num_z - b
        res = 'a'*num_a + chr(q+97)*b + 'z'*num_z
        return res