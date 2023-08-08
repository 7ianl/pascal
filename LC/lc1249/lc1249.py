class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q, s = list(s), list()
        for i, c in enumerate(q):
            if c == '(':
                s.append(i)
            elif c == ')':
                if s:
                    s.pop()
                else:
                    q[i] = ''
        for n in s:
            q[n] = ''
        return ''.join(q)