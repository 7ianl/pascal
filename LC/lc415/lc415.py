class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def addstr(s1, s2):
            ###s1.length >= s2.length 
            res = []
            carry = 0
            p, q = len(s1)-1, len(s1)-len(s2)
            while carry or p >= 0:
                if p < 0:
                    res.append(carry)
                    carry = 0
                else:
                    n = int(s1[p])
                    if p>=q:
                        n += int(s2[p-q])+carry
                    else:
                        n += carry
                    res.append(n%10)
                    carry = n//10
                p -= 1
            res.reverse()
            return ''.join(list(map(str, res)))
        return addstr(num1, num2) if len(num1) >= len(num2) else addstr(num2, num1)