class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['init']
        for i in range(len(s)):
            x = s[i]
            if x == '{' or x == '[' or x == '(':
                stack.append(x)
            elif x == '}':
                if stack [-1] == '{':
                    stack.pop()
                else:
                    return False
            elif x == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif x == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return stack == ['init']