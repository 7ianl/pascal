class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply1d(s, k):
            res = []
            carry = 0
            for i in range(len(s)-1, -1, -1):
                n = int(s[i])*k+carry
                res.append(n%10)
                carry = n//10
            if carry:
                res.append(carry)
            res.reverse()
            return ''.join(list(map(str, res)))
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
        def multiplynd(s1, s2):
            ###s1.length >= s2.length
            nums = []
            L = len(s2)
            for i in range(L):
                acc = multiply1d(s1, int(s2[L-i-1])) + '0'*i
                nums.append(acc)
            nums.sort(key= lambda x: len(x), reverse=True)
            res = nums[0]
            for i in range(1, len(nums)):
                res = addstr(res, nums[i])
            return res
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) >= len(num2):
            return multiplynd(num1, num2)
        else:
            return multiplynd(num2, num1)