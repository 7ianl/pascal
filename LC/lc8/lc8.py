class Solution:
    def myAtoi(self, s: str) -> int:
        def isInt(x):
            return True if '0' <= x <= '9' else False
        def AtoiHelper(s):
            output = 0
            for x in s:
                if isInt(x):
                    output *= 10
                    output += (ord(x)-48)
                else:
                    break
            return output
        for x in range(len(s)):
            if isInt(s[x]) == True:
                x = AtoiHelper(s[x:])
                if x > (2**31 - 1):
                    return 2**31 - 1
                else:
                    return x
            elif s[x] == ' ':
                continue
            elif s[x] == '-':
                x = AtoiHelper(s[(x+1):])
                if x > 2**31 :
                    return -2**31
                else:
                    return -1 * x
            elif s[x] == '+':
                x = AtoiHelper(s[(x+1):])
                if x > (2**31 - 1):
                    return 2**31 - 1
                else:
                    return x
            else:
                return 0
        return 0