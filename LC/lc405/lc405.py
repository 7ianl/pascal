class Solution:
    def toHex(self, num: int) -> str:
        d = ('0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e',
            'f')
        res = []
        if num < 0:
            num += 16 ** 8
        if num == 0:
            return '0'
        while num:
            res.append(d[num%16])
            num //= 16
        res.reverse()
        return ''.join(res)