class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def ListGen(res: list, Letters: list) -> list:
            out = []
            for x in Letters:
                add = res[:]
                for y in range(len(add)):
                    add[y] += x
                out.extend(add)
            return out
        corresp = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        def getCorresp(x: str) -> List[str]:
            return corresp[(ord(x) - ord('2'))]
        if digits == '':
            return []
        else:
            res = getCorresp(digits[0])
            digits = digits[1:]
        while digits:
            res = ListGen(res, getCorresp(digits[0]))
            digits = digits[1:]
        return res