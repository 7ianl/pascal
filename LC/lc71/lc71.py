class Solution:
    def simplifyPath(self, path: str) -> str:
        path += '/'
        paths = list()
        stack = ''
        for i in range(len(path)):
            if path[i] == '/':
                if stack == '':
                    continue
                else:
                    if stack == '..':
                        if paths:
                            paths.pop()
                    elif stack == '.':
                        stack = ''
                        continue
                    else: paths.append(stack)
                    stack = ''
            else:
                stack += path[i]
        res = '/' + ('/').join(paths)
        return res