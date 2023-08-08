class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        isPositive = x >= 0
        answer = 0
        x = abs(x)
        while 1:
            stack.append(x % 10)
            x //= 10
            if x == 0:
                break
        for x in stack:
            answer *= 10
            answer += x
        if not isPositive:
            answer *= -1
        if abs(answer) > (2**31 -1):
            answer = 0
        return answer