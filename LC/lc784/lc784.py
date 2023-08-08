class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        stack = list()
        for c in S:
            if c.islower():
                stack.append((c, c.upper()))
            elif c.isupper():
                stack.append((c, c.lower()))
            else:
                stack.append(c)
        if type(stack[0]) == tuple:
            res = [stack[0][0], stack[0][1]]
        else:
            res = [stack[0]]
 
        for item in stack[1:]:
            if type(item) == tuple:
                l,r = item[0], item[1]
                left = [x+l for x in res]
                right = [x+r for x in res]
                left.extend(right)
                res = left
            else:
                res = [x+item for x in res]
        return res